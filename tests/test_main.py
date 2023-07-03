import click.testing
import pytest

from inspyre import main


@pytest.fixture
def runner():
    return click.testing.CliRunner()


def test_main_succeeds(rner):
    result = rner.invoke(main.main)
    assert result.exit_code == 0
