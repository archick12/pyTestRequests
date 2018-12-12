# pyTestRequests

![alt text](https://github.com/archick12/pyTestRequests/blob/master/Structure.png)

# To run tests
python3 -m pytest --alluredir ./reports
allure generate -c ./reports
allure serve ./reports


# Configuration files
// TODO

# Troubleshooting
```python
import file mismatch:
HINT: remove __pycache__ / .pyc files and/or use a unique basename for your test file modules
```

SOLUTION:
```bash
apiliuk$ cd pyTestRequests/
apiliuk$ rm -rf __pycache__/
apiliuk$ rm -rf tests/__pycache__/
apiliuk$ rm -rf tests/draft/__pycache__/
```
