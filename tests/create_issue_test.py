import pytest
from requests import Response
from tests.utils.api import Api


class TestIssueRefactored:

    @staticmethod
    def setup():
        assert 1 == 1

    @staticmethod
    def teardown():
        assert 1 == 1

    @pytest.mark.api
    def test_create_issue_refactored(self):
        result: Response = Api.create_issue("WEBINAR")

        assert 201 == result.status_code
        response_json = result.json()

        ticket_id = response_json["id"]
        result = Api.delete_issue(ticket_id)
        assert 204 == result.status_code
