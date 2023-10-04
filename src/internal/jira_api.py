from jira import JIRA

from src.internal.secrets import JIRA_TOKEN, JIRA_EMAIL


def get_jira() -> JIRA:
    return JIRA(
        'https://runkeeper.atlassian.net/',
        basic_auth=(
            JIRA_EMAIL,
            JIRA_TOKEN
        )
    )
