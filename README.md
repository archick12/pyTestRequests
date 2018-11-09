# pyTestRequests

# To run tests
python3 -m pytest -n 4 tests --alluredir ./reports
allure generate -c ./reports
allure serve ./reports


# For config gile
 Add additional arguments: --tc-file=test_config.py --tc-format=python -p no:cacheprovider


# Config parser may not find config file if working directory is test and not a projects root directory