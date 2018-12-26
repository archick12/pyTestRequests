import pytest
from tests.utils.api import Api


@pytest.fixture(scope="function", autouse=True)
def pytest_runtest_setup():
    Api.login()
    yield
