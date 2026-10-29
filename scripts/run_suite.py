"""Run one suite and expose only numeric TestOps IDs, never the full environment."""
import os
from pathlib import Path
import shlex
import subprocess
import sys


def main():
    suite = sys.argv[1]
    if suite not in {"unit", "functional"}:
        raise SystemExit("Unknown suite")
    env = os.environ.copy()
    for key in ("ALLURE_ENDPOINT", "ALLURE_TOKEN", "ALLURE_PROJECT_ID"):
        if not env.get(key):
            raise SystemExit(f"Missing {key}")
    for key in ("ALLURE_JOB_RUN_ID", "ALLURE_LAUNCH_ID"):
        env.pop(key, None)
    uid = f'{env["GITHUB_RUN_ID"]}-{env["GITHUB_RUN_ATTEMPT"]}-{env["GITHUB_JOB"]}'
    env.update(
        ALLURE_JOB_RUN_UID=uid,
        ALLURE_JOB_RUN_NAME=env["GITHUB_JOB"],
        ALLURE_JOB_RUN_URL=f'{env["GITHUB_SERVER_URL"]}/{env["GITHUB_REPOSITORY"]}/actions/runs/{env["GITHUB_RUN_ID"]}',
        ALLURE_LAUNCH_NAME=f'{env["GITHUB_REPOSITORY"]} - {suite} - {uid}',
    )
    print(f"Requested Job Run UID: {uid}", flush=True)
    result = subprocess.run([
        "./allurectl", "watch", "--", sys.executable, "-m", "pytest",
        f"tests/{suite}", f'--alluredir={env["ALLURE_RESULTS"]}',
    ], env=env)
    info = subprocess.run(["./allurectl", "job-run", "env"], env=env,
                          capture_output=True, text=True)
    if info.returncode:
        raise SystemExit("Cannot retrieve Job Run environment; see watch log")
    values = dict(token.split("=", 1) for token in shlex.split(info.stdout)
                  if "=" in token)
    ids = {}
    for key in ("ALLURE_LAUNCH_ID", "ALLURE_JOB_RUN_ID"):
        value = values.get(key, "")
        if not value.isascii() or not value.isdecimal() or int(value) <= 0:
            raise SystemExit(f"Missing or invalid {key} in job-run env")
        ids[key] = value
    print(f'Launch ID: {ids["ALLURE_LAUNCH_ID"]}; Job Run ID: {ids["ALLURE_JOB_RUN_ID"]}')
    with Path(env["GITHUB_OUTPUT"]).open("a") as output:
        output.write(f'launch_id={ids["ALLURE_LAUNCH_ID"]}\n')
        output.write(f'job_run_id={ids["ALLURE_JOB_RUN_ID"]}\n')
    raise SystemExit(result.returncode)


if __name__ == "__main__":
    main()
