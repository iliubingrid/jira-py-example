import requests
import json
from requests.auth import HTTPBasicAuth

from src.internal.secrets import JIRA_TOKEN, JIRA_EMAIL


def load_file(file_path: str):
    f = open(file_path, mode="r")
    all_of_it = f.read()
    f.close()
    return all_of_it


# set auth token and get the basic auth code
auth_token = JIRA_TOKEN
basic_auth = HTTPBasicAuth(JIRA_EMAIL, auth_token)

# Set the title and content of the page to create
page_title = 'My New Page10'
# page_html = '<p>This page was created with Python!</p>'
page_html = load_file("report.html")
    # .replace("<html>", "<div>").replace("</html>", "</div>")\
    # .replace("<head>", "<div>").replace("</head>", "</div>")\
    # .replace("<body>", "<div>").replace("</body>", "</div>")\
    # .replace("\n", "").replace("  ", " ").replace("  ", " ").replace("  ", " ")



parent_page_id = 3781099776
space_key = 'ECMS'

# get the confluence home page url for your organization {confluence_home_page}
url = 'https://runkeeper.atlassian.net/wiki/rest/api/content/'

# Request Headers
headers = {
    'Content-Type': 'application/json;charset=iso-8859-1',
}

# Request body
data = {
    'type': 'page',
    'title': page_title,
    'ancestors': [{'id': parent_page_id}],
    'space': {'key': space_key},
    'body': {
        'storage': {
            'value': page_html,
            'representation': 'storage',
        }
    }
}

# We're ready to call the api
try:

    r = requests.post(url=url, data=json.dumps(data), headers=headers, auth=basic_auth)

    # Consider any status other than 2xx an error
    if not r.status_code // 100 == 2:
        print("Error: Unexpected response {}".format(r))
    else:
        print('Page Created!')

except requests.exceptions.RequestException as e:

    # A serious problem happened, like an SSLError or InvalidURL
    print("Error: {}".format(e))
