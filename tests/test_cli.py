from pathlib import Path
# tests/test_cli.py
import pytest
from click.testing import CliRunner
from simple_hosting_capacity.cli import run_hosting_capacity
from simple_hosting_capacity.cli import build_plots

BASE_TEST_PATH = Path(__file__).parent
OPENDSS_PATH = BASE_TEST_PATH / "data" / "Master.dss"
TEST_DUMP = BASE_TEST_PATH / "test_dump"

@pytest.fixture
def runner():
    return CliRunner()

def test_run_hosting_capacity_help(runner):
    result = runner.invoke(run_hosting_capacity, ['--help'])
    assert result.exit_code == 0
    assert 'Usage:' in result.output

def test_run_hosting_capacity_missing_model(runner):
    result = runner.invoke(run_hosting_capacity)
    assert result.exit_code != 0
    assert "Missing argument 'MODEL'" in result.output

def test_run_hosting_capacity_valid_args(runner, tmp_path):
    export_path = tmp_path / 'export.csv'
    result = runner.invoke(run_hosting_capacity, [str(OPENDSS_PATH), '-l', '100', '-h', '200', '-f', '1', '-p', '1', '-a', '1', '-m', '1', '-t', '1', '-e', str(TEST_DUMP)])
    assert result.exit_code == 0
    assert TEST_DUMP.exists()