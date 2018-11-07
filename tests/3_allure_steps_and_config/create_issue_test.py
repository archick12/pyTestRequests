from requests import Response
from utils.api_manager import ApiManager


class TestIssueRefactored:

    def setup(self):
        a = 0
        # ApiManager.login()

    def test_create_issue_refactored(self):
        result: Response = ApiManager.create_issue("WEBINAR")

        assert 201 == result.status_code
        response_json = result.json()

        ticket_id = response_json["id"]
        result = ApiManager.delete_issue(ticket_id)
        assert 204 == result.status_code
