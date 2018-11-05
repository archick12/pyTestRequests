import requests


class TestLogin:

    def test_create_issue(self):
        result = requests.get('http://jira.hillel.it:8080',
                              auth=('webinar5', 'webinar5'))
        assert 200 == result.status_code
        cookie = {'JSESSIONID': result.cookies.get("JSESSIONID")}

        json_for_create_issue = {
            "fields": {
                "project":
                    {
                        "key": "WEBINAR"
                    },
                "summary": "Test Summary",
                "description": "Creating of an issue",
                "assignee": {"name": "webinar5"},
                "priority": {"name": "High"},
                "issuetype": {"name": "Bug"}
            }
        }

        result = requests.post("http://jira.hillel.it:8080/rest/api/2/issue",
                               json=json_for_create_issue,
                               headers={'Content-Type': 'application/json'},
                               cookies=cookie)
        assert 201 == result.status_code
        response_json = result.json()
        print(response_json)

        result = requests.delete("http://jira.hillel.it:8080/rest/api/2/issue/" + response_json["id"],
                               headers={'Content-Type': 'application/json'},
                               cookies=cookie)
        assert 204 == result.status_code

