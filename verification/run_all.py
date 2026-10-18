"""Run the finite checks and compare their JSON outputs with expected results."""
import json
import math
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
CHECKS = (
    "verify_operator_bounds.py",
    "verify_fresh_likelihood.py",
    "verify_syndromes.py",
)


def compare(actual, expected, context):
    if isinstance(expected, dict):
        if not isinstance(actual, dict) or actual.keys() != expected.keys():
            raise AssertionError(f"{context}: result keys differ")
        for key in expected:
            compare(actual[key], expected[key], f"{context}.{key}")
    elif isinstance(expected, list):
        if not isinstance(actual, list) or len(actual) != len(expected):
            raise AssertionError(f"{context}: result lengths differ")
        for index, (a, e) in enumerate(zip(actual, expected)):
            compare(a, e, f"{context}[{index}]")
    elif isinstance(expected, float):
        if not isinstance(actual, (float, int)) or not math.isclose(
            actual, expected, rel_tol=1e-9, abs_tol=2e-10
        ):
            raise AssertionError(f"{context}: {actual!r} differs from {expected!r}")
    elif actual != expected:
        raise AssertionError(f"{context}: {actual!r} differs from {expected!r}")


def main():
    summaries = {}
    for filename in CHECKS:
        completed = subprocess.run(
            [sys.executable, str(HERE / filename)],
            cwd=HERE.parent,
            check=True,
            capture_output=True,
            text=True,
        )
        actual = json.loads(completed.stdout)
        expected_path = HERE / "expected" / Path(filename).with_suffix(".json")
        expected = json.loads(expected_path.read_text())
        compare(actual, expected, filename)
        summaries[filename] = actual
        print(f"PASS {filename}")
    print(json.dumps({"checks_passed": len(summaries)}, indent=2))


if __name__ == "__main__":
    main()
