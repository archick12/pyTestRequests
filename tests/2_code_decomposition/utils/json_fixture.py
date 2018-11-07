class JSONFixture:

    @staticmethod
    def for_create_issue(projectKey):
        json = {
            "fields": {
                "project":
                    {
                        "key": projectKey
                    },
                "summary": "Test Summary",
                "description": "Creating of an issue",
                "assignee": {"name": "webinar5"},
                "priority": {"name": "High"},
                "issuetype": {"name": "Bug"}
            }
        }
        return json
