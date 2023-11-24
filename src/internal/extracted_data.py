import string
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import List

from jira import Issue
from pytz import UTC

from src.internal.domain import SPRINT_A_START_TIME
from src.internal.enums import TeamEnum
from src.internal.team_members import (ADI_TEAM_MEMBERS, CAP_TEAM_MEMBERS,
                                       GRID_TEAM_MEMBERS)


@dataclass
class ExtractedData:
    issue_id: str
    issue_type: str
    status: str
    reporter: str
    sprints: List[str]
    story_points: int
    created_at: str
    resolved_at: str
    labels: List[str]

    first_sprint: str
    last_sprint: str
    team: TeamEnum
    reporter_team: TeamEnum
    summary: str


def labels_2_team(labels: List[str]) -> TeamEnum:
    if "Grid" in labels:
        return TeamEnum.GRID
    if "capgemini" in labels or "next.js" in labels:
        return TeamEnum.CAP
    if "ADI" in labels:
        return TeamEnum.ADI
    return TeamEnum.UNDEFINED


def reporter_2_team(reporter: str) -> TeamEnum:
    if reporter in GRID_TEAM_MEMBERS:
        return TeamEnum.GRID
    if reporter in CAP_TEAM_MEMBERS:
        return TeamEnum.CAP
    if reporter in ADI_TEAM_MEMBERS:
        return TeamEnum.ADI
    return TeamEnum.UNDEFINED


def resolve_story_points(value) -> int:
    if value is None:
        return 0
    return int(value)


def resolve_sprint_letter(full_sprint_name: str) -> str:
    if full_sprint_name == "Discovery":
        return "0"
    if full_sprint_name == "":
        return ""
    return full_sprint_name[0]


def date_2_sprint(date: str) -> str:
    if not date:
        return ""
    date = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f%z").astimezone(UTC)
    prev_date = SPRINT_A_START_TIME
    for s in string.ascii_uppercase:
        prev_date = prev_date + timedelta(days=14)
        if date < prev_date:
            return s
    return "UNDEFINED_SPRINT"


def resolve_first_sprint(created_date):
    return date_2_sprint(created_date)


def resolve_last_sprint(resolution_date):
    return date_2_sprint(resolution_date)


def issue_2_data(issue: Issue) -> ExtractedData:
    sprints: List[str] = []
    if issue.fields.customfield_10200:
        sprints = sorted([s.name for s in issue.fields.customfield_10200])

    return ExtractedData(
        issue_id=issue.key,
        issue_type=issue.fields.issuetype.name,
        status=issue.fields.status.name,
        reporter=issue.fields.reporter.displayName,
        sprints=sprints,
        story_points=resolve_story_points(issue.fields.customfield_10004),
        created_at=issue.fields.created,
        resolved_at=issue.fields.resolutiondate,
        labels=issue.fields.labels,
        first_sprint=resolve_first_sprint(issue.fields.created),
        last_sprint=resolve_last_sprint(issue.fields.resolutiondate),
        team=labels_2_team(issue.fields.labels),
        reporter_team=reporter_2_team(issue.fields.reporter.displayName),
        summary=issue.fields.summary,
    )
