import pytest
import os


# will be always executed before each test
@pytest.fixture(scope="function", autouse=True)
def pytest_runtest_setup():
   # TODO Doesn't work. Overrides...  ApiManagerLogging.BASE_URL = config['jira']['url']
    1==1