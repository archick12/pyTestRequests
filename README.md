# pyTestRequests

# To run tests
python3 -m pytest --alluredir ./reports
allure generate -c ./reports
allure serve ./reports


# Configuration files
// TODO

# Troubleshooting
import file mismatch:
imported module 'tests.draft.login_test' has this __file__ attribute:
  /Users/apiliuk/Downloads/pyTestRequests/tests/1/login_test.py
which is not the same as the test file we want to collect:
  /Users/apiliuk/Downloads/pyTestRequests/tests/draft/login_test.py
HINT: remove __pycache__ / .pyc files and/or use a unique basename for your test file modules


SOLUTION:
apiliuk$ cd pyTestRequests/
apiliuk$ rm -rf __pycache__/
apiliuk$ rm -rf tests/__pycache__/
apiliuk$ rm -rf tests/draft/__pycache__/