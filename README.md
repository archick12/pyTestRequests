# pyTestRequests

![alt text](https://github.com/archick12/pyTestRequests/blob/master/Structure.png)

# To run tests
1. python3 -m pytest  -p no:cacheprovider  --alluredir ./reports
2. allure generate -c ./reports
3. allure serve ./reports


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
