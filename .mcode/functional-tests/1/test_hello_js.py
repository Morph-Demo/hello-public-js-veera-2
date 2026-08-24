"""
Functional tests for hello-public-js-veera-2 (target): hello.js
Tests verify the Node.js script outputs 'Hello Demo' with exit code 0,
matching the behavior of the origin Python script.
"""
import subprocess
import pytest

WORKING_DIR = "/l2l/workspace/hello-public-js-veera-2"


def run_js_script():
    """Helper to invoke hello.js via Node.js and capture output."""
    result = subprocess.run(
        ["node", "hello.js"],
        cwd=WORKING_DIR,
        capture_output=True,
        text=True,
        timeout=30,
    )
    return result


class TestHelloJS:
    """Tests for hello.js — the Node.js target script."""

    def test_hello_exits_zero(self):
        """HAPPY_PATH: Node.js script exits with code 0."""
        result = run_js_script()
        assert result.returncode == 0

    def test_hello_stdout_exact(self):
        """HAPPY_PATH: Node.js script outputs exactly 'Hello Demo' followed by a newline."""
        result = run_js_script()
        assert result.stdout.strip() == "Hello Demo"

    def test_hello_no_stderr(self):
        """HAPPY_PATH: Node.js script produces no stderr output."""
        result = run_js_script()
        assert result.stderr == ""

    def test_hello_stdout_matches_origin(self):
        """HAPPY_PATH: Node.js stdout matches the Python origin output."""
        js_result = run_js_script()
        origin_result = subprocess.run(
            ["python3", "hello.py"],
            cwd="/l2l/workspace/hello-public",
            capture_output=True,
            text=True,
            timeout=30,
        )
        assert js_result.stdout.strip() == origin_result.stdout.strip()
