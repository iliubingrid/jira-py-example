import matplotlib.pyplot as plt

from src.internal.csv_helper import read_from_csv_file
from src.internal.dict_helper import sort_dict, default_int_dict, remove_keys, accumulate_data
from src.internal.domain import UNUSED_SPRINTS
from src.internal.enums import TeamEnum
from src.internal.extracted_data import resolve_first_sprint, labels_2_team

lst = read_from_csv_file("tmp/list.csv")

cap_bugs = list(filter(lambda x: (x.issue_type == "Bug" and x.reporter_team == TeamEnum.CAP), lst))
grid_bugs = list(filter(lambda x: (x.issue_type == "Bug" and x.reporter_team == TeamEnum.GRID), lst))

grid_on_cap_bugs = default_int_dict()
for i in grid_bugs:
    team = labels_2_team(i.labels)
    first_sprint = resolve_first_sprint(i.created_at)
    if team == TeamEnum.CAP:
        grid_on_cap_bugs[first_sprint] += 1
cap_on_grid_bugs = default_int_dict()
for i in cap_bugs:
    team = labels_2_team(i.labels)
    first_sprint = resolve_first_sprint(i.created_at)
    if team == TeamEnum.GRID:
        cap_on_grid_bugs[first_sprint] += 1

grid_on_cap_acc = accumulate_data(sort_dict(grid_on_cap_bugs))
cap_on_grid_acc = accumulate_data(sort_dict(cap_on_grid_bugs))

grid_on_cap_acc = sort_dict(remove_keys(grid_on_cap_acc, UNUSED_SPRINTS))
cap_on_grid_acc = sort_dict(remove_keys(cap_on_grid_acc, UNUSED_SPRINTS))

plt.style.use('fivethirtyeight')

plt.plot(
    grid_on_cap_acc.keys(),
    grid_on_cap_acc.values(),
    label="Grid on Cap",
    color="red"
)
plt.plot(
    cap_on_grid_acc.keys(),
    cap_on_grid_acc.values(),
    label="Cap on Grid",
    color="blue"
)

the_table = plt.table(
    cellText=[list(grid_on_cap_acc.values()), list(cap_on_grid_acc.values())],
    rowLabels=["Grid on Cap", "Cap on Grid"],
    colLabels=list(grid_on_cap_acc.keys()),
    loc='bottom'
)
plt.subplots_adjust(left=0.2, bottom=0.2)
the_table.auto_set_font_size(False)
the_table.set_fontsize(8)
plt.xticks([])

# plt.xlabel('Sprints')
plt.ylabel('Issues')
plt.title('Accumulated defects by counter-parts')
plt.legend()
plt.show()
