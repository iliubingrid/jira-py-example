from jira import JIRA

from src.internal._secrets import JIRA_EMAIL, JIRA_TOKEN


def get_jira() -> JIRA:
    return JIRA(
        'https://runkeeper.atlassian.net/',
        basic_auth=(
            JIRA_EMAIL,
            JIRA_TOKEN
        )
    )
