#!/usr/bin/env python3
"""Runs scripts/submission/tests/ and reads the count, not just the exit code.

    python3 scripts/submission/run_tests.py

A run that ran fewer than MIN_TESTS tests fails even when unittest says OK (a discovery pattern or
import that silently matches nothing would otherwise read as a pass). Prints `ran N tests`.
"""
import sys
import unittest
from pathlib import Path

sys.dont_write_bytecode = True
TESTS = Path(__file__).resolve().parent / "tests"
MIN_TESTS = 140


def main() -> int:
    sys.path.insert(0, str(TESTS))
    suite = unittest.defaultTestLoader.discover(str(TESTS), pattern="test_*.py", top_level_dir=str(TESTS))
    result = unittest.TextTestRunner(verbosity=1).run(suite)
    ran, skipped = result.testsRun, len(result.skipped)
    print(f"ran {ran} tests ({skipped} skipped), {len(result.failures)} failures, {len(result.errors)} errors")
    if not result.wasSuccessful():
        return 1
    if ran - skipped < MIN_TESTS:
        print(f"::error::only {ran - skipped} submission tests ran (not skipped); expected at least {MIN_TESTS}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
