import requests
from pytest_testconfig import config
from allure_commons._allure import step

from utils.json_fixture import JSONFixture


class ApiManager:

    BASE_URL = "http://jira.hillel.it:8080"
    CREATE_ISSUE = BASE_URL + "/rest/api/2/issue/"
    DELETE_ISSUE = BASE_URL + "/rest/api/2/issue/{0}/"

    headers = {'Content-Type': 'application/json'}
    cookie = ""

    @staticmethod
    def login():
        with step("Login"):
            result = requests.get(ApiManager.BASE_URL,
                                  auth=("webinar5","webinar5"))
            assert 200 == result.status_code
            ApiManager.cookie = {'JSESSIONID': result.cookies.get("JSESSIONID")}

    @staticmethod
    def create_issue(project_key):
        with step("Create issue"):
            result = requests.post(ApiManager.CREATE_ISSUE,
                                   json=JSONFixture.for_create_issue(project_key),
                                   headers=ApiManager.headers,
                                   cookies=ApiManager.cookie)
            return result

    # @allure.step - will not work as expected. Returned value will be a link to memory
    @staticmethod
    def delete_issue(issue_id):
        with step("Delete issue by ID"):
            result = requests.delete(ApiManager.DELETE_ISSUE.format(issue_id),
                                     headers=ApiManager.headers,
                                     cookies=ApiManager.cookie)
            return result
