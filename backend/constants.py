from utils import load_slo_configs

TABLE_ID = 'rnm-shared-monitoring.slos.last_report'
FILTER_KEYS = [
    "service_name",
    "feature_name",
    "slo_name",
    "alert",
    "window",
    "metadata",
]
SLO_REPO_PATH = '../../slo-repo'
SLO_CONFIGS_PATHS = [
    '../../slo-repo/slos/**/**',
]
ERROR_BUDGET_POLICY_PATH = '../../slo-repo/slos/error_budget_policy.yaml'
SLO_CONFIGS = load_slo_configs(SLO_CONFIGS_PATHS)
