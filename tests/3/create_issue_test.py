from requests import Response

from utils.api_operations import ApiOperations
from utils.base_api_test import BaseAPITest


class TestIssueRefactored(BaseAPITest):

    def setup(self):
        BaseAPITest.authenticate()

    def test_create_issue_refactored(self):
        result: Response = ApiOperations.create_issue("WEBINAR")

        assert 201 == result.status_code
        response_json = result.json()

        ticket_id = response_json["id"]
        result = ApiOperations.delete_issue(ticket_id)
        assert 204 == result.status_code
