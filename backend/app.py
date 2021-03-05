from flask import Flask, jsonify, Response, request
from google.cloud import bigquery
import json

app = Flask(__name__)
client = bigquery.Client()

TABLE_ID = 'rnm-shared-monitoring.slos.last_report'

def bq_query(query):
    """Run a BigQuery query job and return a JSON result.

    Args:
        query (string): BigQuery query string.
    
    Returns:
        list: List of records matching the query.
    """
    query_job = client.query(query)
    df = query_job.to_dataframe()
    return df.to_json(orient='records')

def parse_window(window):
    window_seconds = 0
    if isinstance(window, int): # time already converted
        return window
    if 'd' in window:
        split = window.split('d')
        window_seconds += int(split[0]) * 24 * 60 * 60
        window = split[-1]
    if 'h' in window:
        split = window.split('h')
        window_seconds += int(split[0]) * 60 * 60
        window = split[-1]
    if 'm' in window:
        split = window.split('m')
        window_seconds += int(split[0]) * 60
        window = split[-1]
    if 's' in window:
        split = window.split('s')
        window_seconds += int(split[0])
    return window_seconds


@app.route('/slos/columns')
def get_columns(search=None):
    columns = [
        "sli_measurement",
        "gap",
        "slo_target",
        "alert",
        "good_events_count",
        "bad_events_count",
        "service_name",
        "feature_name",
        "slo_name",
        "slo_description",
        "window",
        "metadata",
        "error_budget_burn_rate",
        "alerting_burn_rate_threshold",
    ]
    if search:
        columns = [c for c in columns if search in c]
    return columns

@app.route('/slos/fields')
def query_distinct_fields():
    col = request.args.get('col')
    filter_col = col
    if filter_col == 'window':
        filter_col = '`window`'
    query = """
    SELECT DISTINCT({col}) FROM `{TABLE_ID}`
    """
    result = bq_query(query)
    return result


@app.route('/slos/last_report')
def query_last_report():
    offset = request.args.get('offset', 0)
    limit = request.args.get('limit', 100)
    service_name = request.args.get('service_name')
    feature_name = request.args.get('feature_name')
    window = request.args.get('window')
    name = request.args.get('name')
    where_clause = ""
    selectors = []
    if service_name:
        selectors.append(f'service_name = "{service_name}"')
    if feature_name:
        selectors.append(f'feature_name = "{feature_name}"')
    if window:
        window = parse_window(window)
        selectors.append(f'`window` = {window}')
    if name:
        selectors.append(f'slo_name = "{name}"')
    for key, value in request.args.items():
        if key.startswith('metadata'):
            key = key.replace('metadata.', '')
            selectors.append(f' m.key = "{key}" AND m.value = "{value}"')
    app.logger.info(where_clause)
    if selectors:
        selector_string = ' AND '.join(selectors)
        app.logger.info(selector_string)
        where_clause = f"WHERE {selector_string}"
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
    TO_JSON_STRING(m) as m,
    TO_JSON_STRING(metadata) as metadata,
    AVG(error_budget_burn_rate) as error_budget_burn_rate,
    AVG(alerting_burn_rate_threshold) as alerting_burn_rate_threshold,
    FROM `{TABLE_ID}`, UNNEST(metadata) as m
    {where_clause}
    GROUP BY service_name,feature_name,slo_name,slo_description,`window`,metadata,m
    ORDER BY alert DESC, error_budget_burn_rate DESC
    LIMIT {limit} OFFSET {offset}
    """
    app.logger.info(query)
    result = bq_query(query)
    app.logger.info(result)
    return Response(result, mimetype='application/json')


@app.route('/slos/last_report_count')
def count_last_report():
    query = f"""
    SELECT COUNT(*) AS count FROM `{TABLE_ID}`
    """
    result = bq_query(query)
    app.logger.info(result)
    return Response(result, mimetype='application/json')


@app.route('/slos/all_reports')
def query_dataset():
    query_job = client.list_rows(TABLE_ID, max_results=50)
    df = query_job.to_dataframe()
    result = df.to_json(orient='records')
    app.logger.info(result)
    return Response(result, mimetype='application/json')
