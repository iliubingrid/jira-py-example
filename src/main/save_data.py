from typing import List

from src.internal.extracted_data import ExtractedData, issue_2_data
from src.internal.csv_helper import save_to_csv_file
from src.internal.jira_api import get_jira

jira = get_jira()

issues_total = jira.search_issues('project=ECMS', maxResults=1).total

issues_in_proj = []
for i in range(0, issues_total, 100):
    issues = jira.search_issues('project=ECMS', maxResults=100, startAt=i)
    issues_in_proj.append(issues)

lst: List[ExtractedData] = []
for part in issues_in_proj:
    for data in part:
        lst.append(issue_2_data(data))

file_name = "tmp/list.csv"
save_to_csv_file(file_name, lst)
