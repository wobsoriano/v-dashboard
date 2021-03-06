from flask import Flask, jsonify, Response, request
from google.cloud import bigquery
import json

app = Flask(__name__)
client = bigquery.Client()

TABLE_ID = 'rnm-shared-monitoring.slos.last_report'
FILTER_KEYS = [
    "service_name",
    "feature_name",
    "slo_name",
    "alert",
    "window",
    "metadata",
]

@app.route('/slos/keys')
def get_columns():
    """List all BigQuery column names matching a query.
    
    Args:
        q (str): Query (partial string containing column).

    Returns:
        list: List of columns matching query.
    """
    q = request.args.get('q')
    if not q:
        return jsonify([])
    result = [c for c in FILTER_KEYS if q in c]
    app.logger.info(result)
    return jsonify(result)


@app.route('/slos/values')
def query_distinct_fields():
    """List all BigQuery column values corresponding to column name.

    Args:
        q (str): BigQuery table column name.

    Returns:
        list: List of results from BigQuery.
    """
    q = request.args.get('q').replace(':', '')
    column = q
    if q == 'window':
        column = '`window`'
    if column == 'metadata':
        column = 'metadata.key'
        query = f"""
        SELECT DISTINCT(metadata.key) FROM `{TABLE_ID}`, UNNEST(metadata) as metadata
        """
        result = run_bq_query(query)
        result = [elem["key"] for elem in json.loads(result)]
    else:
        query = f"""
        SELECT DISTINCT({column}) FROM `{TABLE_ID}`
        """
        app.logger.info(query)
        result = run_bq_query(query)
        result = [elem[q] for elem in json.loads(result)]
    app.logger.info(result)
    return jsonify(result)

@app.route('/slos/last_report')
def query_last_report():
    """Query last report table.

    Args:
        offset (int): Offset to start query.
        limit (int): Number of elements to return in response.
        **args (dict): Filter arguments.

    Returns:
        list: List of results from BigQuery.
    """
    offset = request.args.get('offset', 0)
    limit = request.args.get('limit', 100)
    where_clause = build_where_clause(request.args)
    query = f"""
    SELECT
    AVG(sli_measurement) as sli_measurement,
    AVG(gap) as gap,
    AVG(slo_target) AS slo_target,
    MAX(alert) as alert,
    MAX(good_events_count) as good_events_count,
    MAX(bad_events_count) as bad_events_count,
    service_name,
    feature_name,
    slo_name,
    slo_description,
    `window`,
    TO_JSON_STRING(metadata) as metadata,
    AVG(error_budget_burn_rate) as error_budget_burn_rate,
    AVG(alerting_burn_rate_threshold) as alerting_burn_rate_threshold,
    FROM `{TABLE_ID}`, UNNEST(metadata) as m
    {where_clause}
    GROUP BY service_name,feature_name,slo_name,slo_description,`window`,metadata
    ORDER BY alert DESC, error_budget_burn_rate DESC
    LIMIT {limit} OFFSET {offset}
    """
    app.logger.info(query)
    result = run_bq_query(query)
    app.logger.info(result)
    return Response(result, mimetype='application/json')


@app.route('/slos/last_report_count')
def count_last_report():
    query = f"""
    SELECT COUNT(*) AS count FROM `{TABLE_ID}`
    """
    result = run_bq_query(query)
    app.logger.info(result)
    return Response(result, mimetype='application/json')


@app.route('/slos/all_reports')
def query_dataset():
    query_job = client.list_rows(TABLE_ID, max_results=50)
    df = query_job.to_dataframe()
    result = df.to_json(orient='records')
    app.logger.info(result)
    return Response(result, mimetype='application/json')


def build_where_clause(filters):
    """Build WHERE clause to append to an SQL query.
    
    Args:
        filters (dict): Dict of filters to add to the query.

    Returns:
        str: WHERE clause to add to an SQL query.
    """
    selectors = []
    where_clause = ""
    for key, value in request.args.items():
        if key == 'window':
            window = parse_window(value)
            selectors.append(f'`{key}` = {window}')
        elif key.startswith('metadata.'):
            key = key.replace('metadata.', '')
            selectors.append(f' m.key = "{key}" AND m.value = "{value}"')
        elif key not in FILTER_KEYS:
            continue
        else:
            selectors.append(f'{key} = "{value}"')
    if selectors:
        selector_string = ' AND '.join(selectors)
        app.logger.info(selector_string)
        where_clause = f"WHERE {selector_string}"
    return where_clause


def run_bq_query(query):
    """Run a BigQuery query job and return a JSON result.

    Args:
        query (string): BigQuery query string.
    
    Returns:
        list: List of records matching the query.
    """
    query_job = client.query(query)
    df = query_job.to_dataframe()
    return df.to_json(orient='records')


def parse_window(time):
    """Convert a string in the format 'Wd Xh Ym Zs' into an int in seconds.

    Args:
        time (str): A string in the format 'Wd Xh Ym Zs'.

    Returns:
        int: Number of seconds.
    """
    time_seconds = 0
    if isinstance(time, int):  # time already converted
        return time
    if 'd' in time:
        split = time.split('d')
        time_seconds += int(split[0]) * 24 * 60 * 60
        time = split[-1]
    if 'h' in time:
        split = time.split('h')
        time_seconds += int(split[0]) * 60 * 60
        time = split[-1]
    if 'm' in time:
        split = time.split('m')
        time_seconds += int(split[0]) * 60
        time = split[-1]
    if 's' in time:
        split = time.split('s')
        time_seconds += int(split[0])
    return time_seconds
