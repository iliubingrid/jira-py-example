import matplotlib.pyplot as plt

from src.internal.csv_helper import read_from_csv_file
from src.internal.dict_helper import sort_dict, default_int_dict, remove_keys
from src.internal.domain import UNUSED_SPRINTS
from src.internal.enums import TeamEnum
from src.internal.extracted_data import resolve_first_sprint, labels_2_team

lst0 = read_from_csv_file("tmp/list.csv")

# select bugs
bugs = list(filter(lambda x: (x.issue_type == "Bug"), lst0))

grid_bugs = default_int_dict()
cap_bugs = default_int_dict()
for i in bugs:
    team = labels_2_team(i.labels)
    first_sprint = resolve_first_sprint(i.created_at)
    if team == TeamEnum.UNDEFINED:
        continue
    if team == TeamEnum.ADI:
        continue
    if team == TeamEnum.GRID:
        grid_bugs[first_sprint] += 1
    if team == TeamEnum.CAP:
        cap_bugs[first_sprint] += 1

grid_bugs = sort_dict(remove_keys(grid_bugs, UNUSED_SPRINTS))
cap_bugs = sort_dict(remove_keys(cap_bugs, UNUSED_SPRINTS))

plt.style.use('fivethirtyeight')

plt.plot(
    grid_bugs.keys(),
    grid_bugs.values(),
    label="Grid",
    color="blue"
)
plt.plot(
    cap_bugs.keys(),
    cap_bugs.values(),
    label="Cap",
    color="red"
)

the_table = plt.table(
    cellText=[list(grid_bugs.values()), list(cap_bugs.values())],
    rowLabels=["Grid", "Cap"],
    colLabels=list(grid_bugs.keys()),
    loc='bottom'
)
plt.subplots_adjust(left=0.2, bottom=0.2)
the_table.auto_set_font_size(False)
the_table.set_fontsize(8)
plt.xticks([])

# plt.xlabel('Sprints')
plt.ylabel('Issues')
plt.title('Defects Opened per Sprint')
plt.legend()
plt.show()
