import requests

from utils.base_api_test import BaseAPITest
from utils.json_fixture import JSONFixture


class ApiOperations:

    BASE_URL = 'http://jira.hillel.it:8080'
    CREATE_ISSUE = BASE_URL + "/rest/api/2/issue/"
    DELETE_ISSUE = BASE_URL + "/rest/api/2/issue/{0}/"

    @staticmethod
    def create_issue(project_key):
        result = requests.post(ApiOperations.CREATE_ISSUE,
                               json=JSONFixture.for_create_issue(project_key),
                               headers=BaseAPITest.headers,
                               cookies=BaseAPITest.cookie)
        return result

    @staticmethod
    def delete_issue(issue_id):
        result = requests.delete(ApiOperations.DELETE_ISSUE.format(issue_id),
                                 headers=BaseAPITest.headers,
                                 cookies=BaseAPITest.cookie)
        return result
