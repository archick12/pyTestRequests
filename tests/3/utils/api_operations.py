import requests
from allure_commons._allure import step

from utils.base_api_test import BaseAPITest
from utils.json_fixture import JSONFixture


class ApiOperations:

    BASE_URL = 'http://jira.hillel.it:8080'
    CREATE_ISSUE = BASE_URL + "/rest/api/2/issue/"
    DELETE_ISSUE = BASE_URL + "/rest/api/2/issue/{0}/"

    @staticmethod
    def create_issue(project_key):
        with step("Create issue"):
            result = requests.post(ApiOperations.CREATE_ISSUE,
                               json=JSONFixture.for_create_issue(project_key),
                               headers=BaseAPITest.headers,
                               cookies=BaseAPITest.cookie)
            return result

    # @allure.step - will not work as expected. Returned value will be a link to memory
    @staticmethod
    def delete_issue(issue_id):
        with step("Delete issue by ID"):
            result = requests.delete(ApiOperations.DELETE_ISSUE.format(issue_id),
                                 headers=BaseAPITest.headers,
                                 cookies=BaseAPITest.cookie)
            return result
