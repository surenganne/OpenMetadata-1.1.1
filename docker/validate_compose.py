"""
Helper functions used for ingestion of sample data into docker by calling airflow dags
"""

import time
from pprint import pprint
from typing import Tuple

import requests
from metadata.utils.logger import log_ansi_encoded_string
from metadata.cli.docker import REQUESTS_TIMEOUT
from requests.auth import HTTPBasicAuth


HEADER_JSON = {"Content-Type": "application/json"}
BASIC_AUTH = HTTPBasicAuth("admin", "admin")


def get_last_run_info() -> Tuple[str, str]:
    """
    Make sure we can pick up the latest run info
    """
    dag_runs = None
    while not dag_runs:
        log_ansi_encoded_string(message="Waiting for DAG Run data...")
        time.sleep(5)
        runs = requests.get(
            "http://localhost:8080/api/v1/dags/sample_data/dagRuns", auth=BASIC_AUTH, timeout=REQUESTS_TIMEOUT
        ).json()
        dag_runs = runs.get("dag_runs")

    return dag_runs[0].get("dag_run_id"), dag_runs[0].get("state")


def print_last_run_logs() -> None:
    """
    Show the logs
    """
    logs = requests.get(
        "http://localhost:8080/api/v1/openmetadata/last_dag_logs?dag_id=sample_data",
        auth=BASIC_AUTH,
        timeout=REQUESTS_TIMEOUT
    ).text
    pprint(logs)


def main():

    state = None
    while state != "success":

        log_ansi_encoded_string(
            message="Waiting for sample data ingestion to be a success. We'll show some logs along the way.",
        )
        dag_run_id, state = get_last_run_info()
        log_ansi_encoded_string(message=f"DAG run: [{dag_run_id}, {state}]")
        print_last_run_logs()
        time.sleep(10)


if __name__ == "__main__":
    main()
