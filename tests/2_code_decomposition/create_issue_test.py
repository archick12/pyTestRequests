import requests

from utils.api_manager import ApiManager
from utils.json_fixture import JSONFixture


class TestLogin:

    def setup(self):
        ApiManager.login()

    def test_create_issue(self):
        result = requests.post(ApiManager.CREATE_ISSUE,
                               json=JSONFixture.for_create_issue("WEBINAR"),
                               headers=ApiManager.headers,
                               cookies=ApiManager.cookie)
        assert 201 == result.status_code
        response_json = result.json()
        print(response_json)

        result = requests.delete(ApiManager.DELETE_ISSUE.format(response_json["id"]),
                                 headers=ApiManager.headers,
                                 cookies=ApiManager.cookie)
        assert 204 == result.status_code
