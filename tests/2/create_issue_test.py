import requests

from utils.api_uri import ApiPath
from utils.base_api_test import BaseAPITest
from utils.json_fixture import JSONFixture


class TestLogin(BaseAPITest):

    def setup(self):
        BaseAPITest.authenticate()

    def test_create_issue(self):
        result = requests.post(ApiPath.CREATE_ISSUE,
                               json=JSONFixture.for_create_issue("WEBINAR"),
                               headers=self.headers,
                               cookies=self.cookie)
        assert 201 == result.status_code
        response_json = result.json()
        print(response_json)

        result = requests.delete(ApiPath.DELETE_ISSUE.format(response_json["id"]),
                                 headers=self.headers,
                                 cookies=self.cookie)
        assert 204 == result.status_code
