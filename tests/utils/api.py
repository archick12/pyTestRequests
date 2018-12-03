import configparser
from allure_commons._allure import step
from tests.utils.http_manager import HttpManager
from tests.utils.json_fixture import JSONFixture


class Api:
    parser = configparser.ConfigParser()
    parser.read('simple.ini')

    BASE_URL = parser.get('jira', 'url')
    CREATE_ISSUE = BASE_URL + "/rest/api/2/issue/"
    DELETE_ISSUE = BASE_URL + "/rest/api/2/issue/{0}/"

    @staticmethod
    def login():
        with step("Login"):
            url = Api.BASE_URL
            user_name = Api.parser.get('jira', 'username')
            password = Api.parser.get('jira', 'password')

            result = HttpManager.auth(url, user_name, password)
            HttpManager.LOGGER.info('Login with {0}, {1} credentials'.format(user_name, password))
            assert 200 == result.status_code

    @staticmethod
    def create_issue(project_key):
        with step("Create issue"):
            result = HttpManager.post(Api.CREATE_ISSUE,
                                      JSONFixture.for_create_issue(project_key))
            HttpManager.LOGGER.info('Create issue. Method: {0}, Data: {1}'.format("POST", JSONFixture.for_create_issue(project_key)))
            return result

    # @allure.step - will not work as expected. Returned value will be a link to memory
    @staticmethod
    def delete_issue(issue_id):
        with step("Delete issue by ID"):
            result = HttpManager.delete(Api.DELETE_ISSUE.format(issue_id))
            HttpManager.LOGGER.info('Delete issue. Method: {0}, URL : {1}'.format("DELETE", Api.DELETE_ISSUE.format(issue_id)))
            return result
