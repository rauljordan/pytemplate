import click.testing
import pytest

from inspyre import example


@pytest.fixture
def runner():
    return click.testing.CliRunner()


def test_main_succeeds(rner):
    result = rner.invoke(example.main)
    assert result.exit_code == 0
