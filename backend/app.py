from flask import Flask, jsonify, Response, request
import constants
import json
import os
import time
import utils

utils.setup_logging()
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


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
    result = [c for c in constants.FILTER_KEYS if q in c]
    # app.logger.debug(result)
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
        SELECT DISTINCT(metadata.key) FROM `{constants.TABLE_ID}`, UNNEST(metadata) as metadata
        """
        result = utils.run_bq_query(query)
        result = [elem["key"] for elem in json.loads(result)]
    else:
        query = f"""
        SELECT DISTINCT({column}) FROM `{constants.TABLE_ID}`
        """
        # app.logger.info(query)
        result = utils.run_bq_query(query)
        result = [elem[q] for elem in json.loads(result)]
    # app.logger.debug(result)
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
    where_clause = utils.build_where_clause(request.args)
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
    FROM `{constants.TABLE_ID}`, UNNEST(metadata) as m
    {where_clause}
    GROUP BY service_name,feature_name,slo_name,slo_description,`window`,metadata
    ORDER BY alert DESC, error_budget_burn_rate DESC
    LIMIT {limit} OFFSET {offset}
    """
    # app.logger.info(query)
    result = utils.run_bq_query(query)
    # app.logger.debug(result)
    return result


@app.route('/slos/last_report_count')
def count_last_report():
    query = f"""
    SELECT COUNT(*) AS count FROM `{constants.TABLE_ID}`
    """
    result = utils.run_bq_query(query)
    # app.logger.debug(result)
    return result


@app.route('/slos/all_reports')
def query_dataset():
    query_job = utils.bq_client.list_rows(constants.TABLE_ID, max_results=50)
    df = query_job.to_dataframe()
    result = df.to_json(orient='records')
    # app.logger.debug(result)
    return result


@app.route('/slo/<name>', methods=['GET'])
def get_slo_config(name):
    return utils.get_slo_config(name)


@app.route('/slo/<name>', methods=['POST'])
def update_slo_config(name):
    data = request.get_json()
    # app.logger.info(data)
    success, error = utils.update_slo_config(name, data)
    return {
        "success": success,
        "errorMessage":
            f"There was an error while updating the configuration on disk. "
            f"Error message: {error}",
        "data": utils.get_slo_config(name)
    }


@app.route('/slo/<name>/diff', methods=['GET'])
def get_slo_staging(name):
    path = utils.get_slo_config(name)['_path']
    diffs = utils.get_current_diff(constants.SLO_REPO_PATH)
    rel_path = os.path.relpath(path, constants.SLO_REPO_PATH)
    # app.logger.info(rel_path)
    # app.logger.info(diffs)
    return {"diff": diffs.get(rel_path)}


@app.route('/slo/<name>/test', methods=['POST'])
def test_slo(name):
    slo_config_path = request.get_json()['_path']

    ebp_config_path = os.path.abspath(constants.ERROR_BUDGET_POLICY_PATH)
    try:
        from slo_generator.utils import parse_config
        from slo_generator.compute import compute
        slo_config = parse_config(slo_config_path)
        ebp_config = parse_config(ebp_config_path)
        timestamp = time.time()
        reports = compute(slo_config,
                          ebp_config,
                          timestamp=timestamp,
                          do_export=False)
        return {"success": True, "data": reports}
    except Exception as e:
        app.logger.exception(e)
        return {"success": False, "errorMessage": f"Test failed: {repr(e)}"}
