import csv

from typing import List

from src.internal.enums import TeamEnum
from src.internal.extracted_data import ExtractedData


def resolve_sprints(value: str) -> List[str]:
    return value.replace("[", "").replace("]", "").replace("'", "").split(", ")


def resolve_labels(value: str) -> List[str]:
    return value.replace("[", "").replace("]", "").replace("'", "").split(", ")


def resolve_team(value: str) -> TeamEnum:
    if value == "GRID":
        return TeamEnum.GRID
    if value == "CAP":
        return TeamEnum.CAP
    if value == "ADI":
        return TeamEnum.ADI
    return TeamEnum.UNDEFINED


def read_from_csv_file(file_name: str) -> List[ExtractedData]:
    lst: List[ExtractedData] = []
    with open(file_name, 'r') as f:
        csvreader = csv.reader(f)
        is_first_row = True
        for row in csvreader:
            if is_first_row:
                is_first_row = False
                continue

            lst.append(ExtractedData(
                issue_id=row[0],
                issue_type=row[1],
                status=row[2],
                reporter_team=resolve_team(row[3]),
                team=resolve_team(row[4]),
                first_sprint=row[5],
                last_sprint=row[6],
                story_points=int(row[7]),
                created_at=row[8],
                resolved_at=row[9],
                reporter=row[10],
                sprints=resolve_sprints(row[11]),
                labels=resolve_labels(row[12])
            ))
    return lst


def save_to_csv_file(file_name: str, lst: List[ExtractedData]):
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([
            "issue_id",
            "issue_type",
            "status",
            "reporter_team",
            "team",
            "first_sprint",
            "last_sprint",
            "story_points",
            "created_at",
            "resolved_at",
            "reporter",
            "sprints",
            "labels"
        ])
        for i in lst:
            writer.writerow([
                i.issue_id,
                i.issue_type,
                i.status,
                i.reporter_team,
                i.team,
                i.first_sprint,
                i.last_sprint,
                i.story_points,
                i.created_at,
                i.resolved_at,
                i.reporter,
                i.sprints,
                i.labels
            ])
