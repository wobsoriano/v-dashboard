import os
from utils import load_slo_configs

# Environment
BIGQUERY_LAST_REPORT_TABLE_ID = os.environ['BIGQUERY_LAST_REPORT_TABLE_ID']
ERROR_BUDGET_POLICY_PATH = os.environ['ERROR_BUDGET_POLICY_PATH']
SLO_REPO_PATH = os.environ['SLO_REPO_PATH']
SLO_CONFIGS_PATHS = os.environ['SLO_CONFIGS_PATHS'].split(',')

# Computed
BIGQUERY_FILTER_KEYS = [
    "service_name",
    "feature_name",
    "slo_name",
    "alert",
    "window",
    "metadata",
]
SLO_CONFIGS = load_slo_configs(SLO_CONFIGS_PATHS)
