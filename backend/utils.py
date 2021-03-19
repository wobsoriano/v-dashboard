from google.cloud import bigquery

from git import Repo
import ruamel.yaml as yaml
from ruamel.yaml import YAML
from ruamel.yaml.scalarstring import FoldedScalarString

from collections.abc import Mapping
from logging.config import dictConfig

import constants
import difflib
import glob
import sys
import logging
import os
import textwrap
import traceback
import utils
import constants

bq_client = bigquery.Client()


#-----------#
# Git utils #
#-----------#
def get_current_diff(repo_path):
    repo = Repo(repo_path)
    diffs = repo.index.diff(None, create_patch=True)
    diffmap = {}
    for diff in diffs:
        path = diff.a_path
        diff_str = diff.diff.decode('utf-8')
        diffmap[path] = diff_str
    return diffmap


#-------------------#
# SLO configs utils #
#-------------------#
def get_slo_config(name):
    """Get an SLO config from disk.

    Args:
        name: Concatenation of the service_name, feature_name and slo_name.

    Returns:
        tuple: SLO config.
    """
    return constants.SLO_CONFIGS[name]


def update_slo_config(name, data):
    """Update an SLO config to disk. Preserves indentation, multi-line strings,
    and top comments using ruamel.yaml. Allows deep updates (nested dict).

    Args:
        name: Concatenation of the service_name, feature_name and slo_name.

    Returns:
        tuple: SLO config.
    """
    yaml = YAML()
    yaml.preserve_quotes = True
    yaml.explicit_start = True
    yaml.width = 80
    try:
        # Load SLO config from disk
        path = get_slo_config(name).get('_path')
        with open(path) as f:
            config = yaml.load(f)

        # Deep-update SLO config with new data
        config = deep_update(config, data)

        # Dump new SLO config to file
        with open(path, 'w') as fp:
            yaml.dump(config, fp)

        # Update global object
        config['_path'] = path
        config['_relpath'] = os.path.relpath(path, constants.SLO_REPO_PATH)
        constants.SLO_CONFIGS[name] = config

    except Exception as e:
        print(traceback.print_exc())
        return False, repr(e)
    return True, ""


def load_slo_configs(glob_paths):
    """Load SLO configs from disk from a set of glob path expressions.
    
    Args:
        glob_paths (list): List of glob paths to load SLO configs from.

    Returns:
        dict: A dict of (name, config) where name is the concatenation of the
        service_name, feature_name and slo_name field (unique), and the config
        is the whole YAML config loaded.
    """
    configs_map = {}
    for expr in glob_paths:
        for slo_config_path in glob.glob(expr):
            with open(slo_config_path) as f:
                cfg = yaml.safe_load(f)
            name = '{service_name}-{feature_name}-{slo_name}'.format(**cfg)
            cfg['_path'] = os.path.abspath(slo_config_path)
            cfg['_relpath'] = os.path.relpath(slo_config_path,
                                              constants.SLO_REPO_PATH)
            configs_map[name] = cfg
    print(f"{len(configs_map.keys())} SLO configs loaded successfully from SLO "
          f"config directories: {glob_paths}")
    return configs_map


#----------------#
# BigQuery utils #
#----------------#
def build_where_clause(filters):
    """Build WHERE clause to append to an SQL query.
    
    Args:
        filters (dict): Dict of filters to add to the query.

    Returns:
        str: WHERE clause to add to an SQL query.
    """
    selectors = []
    where_clause = ""
    for key, value in filters.items():
        if key == 'window':
            window = parse_window(value)
            selectors.append(f'`{key}` = {window}')
        elif key.startswith('metadata.'):
            key = key.replace('metadata.', '')
            selectors.append(f' m.key = "{key}" AND m.value = "{value}"')
        elif key not in constants.FILTER_KEYS:
            continue
        else:
            selectors.append(f'{key} = "{value}"')
    if selectors:
        selector_string = ' AND '.join(selectors)
        where_clause = f"WHERE {selector_string}"
    return where_clause


def run_bq_query(query):
    """Run a BigQuery query job and return a JSON result.

    Args:
        query (string): BigQuery query string.
    
    Returns:
        list: List of records matching the query.
    """
    query_job = bq_client.query(query)
    df = query_job.to_dataframe()
    return df.to_json(orient='records')


#-------------#
# Parse utils #
#-------------#
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


#------------#
# YAML utils #
#------------#
def deep_update(data, new_data):
    """Update a dictionary with new data. Does nested updates. Each update is 
    overwrite-only, this does not append / remove from lists.

    Args:
        data (dict): Input dict.
        new_data (dict): Dict containing updated data.

    Returns:
        dict: Input dict, updated with new data.
    """
    for k, v in new_data.items():
        if k.startswith('_'):  # computed fields, ignore
            continue
        if isinstance(v, Mapping):
            data[k] = deep_update(data[k], v)
        elif isinstance(data[k], FoldedScalarString):
            data[k] = FoldedScalarString(v)
        else:
            data[k] = v
    return data


#--------#
# Others #
#--------#
def setup_logging():
    dictConfig({
        'version': 1,
        'formatters': {
            'default': {
                'format':
                    '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
            }
        },
        'handlers': {
            'wsgi': {
                'class': 'logging.StreamHandler',
                'stream': 'ext://flask.logging.wsgi_errors_stream',
                'formatter': 'default'
            }
        },
        'root': {
            'level': 'INFO',
            'handlers': ['wsgi']
        }
    })
