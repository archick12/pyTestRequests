import pytest

from utils.api_manager import ApiManager


# will be always executed before each test
@pytest.fixture(scope="session", autouse=True)
def authenticate():
    ApiManager.login()
