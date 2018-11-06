class ApiPath:

    BASE_URL = 'http://jira.hillel.it:8080'
    CREATE_ISSUE = BASE_URL + "/rest/api/2/issue/"
    DELETE_ISSUE = BASE_URL + "/rest/api/2/issue/{0}/"
