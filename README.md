# pyTestRequests

![alt text](https://github.com/archick12/pyTestRequests/blob/master/Structure.png)

# To run tests
1. python3 -m pytest  -p no:cacheprovider  --alluredir ./reports
2. allure generate -c ./reports
3. allure serve ./reports


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
