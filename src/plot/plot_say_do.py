import matplotlib.pyplot as plt

from src.internal.csv_helper import read_from_csv_file
from src.internal.dict_helper import default_int_dict, default_float_dict, sort_dict, remove_keys
from src.internal.domain import UNUSED_SPRINTS
from src.internal.enums import TeamEnum
from src.internal.extracted_data import labels_2_team, resolve_first_sprint

lst = read_from_csv_file("tmp/list.csv")

# remove epics
lst2 = list(filter(lambda x: (x.issue_type != "Epic"), lst))
# select closed issues
closed_issues = list(filter(lambda x: (x.status == "Done"), lst2))

grid_do = default_int_dict()
cap_do = default_int_dict()
all_do = default_int_dict()
for i in closed_issues:
    team = labels_2_team(i.labels)
    if team == TeamEnum.UNDEFINED:
        continue
    if team == TeamEnum.ADI:
        continue
    if team == TeamEnum.GRID:
        grid_do[i.last_sprint] += 1
    if team == TeamEnum.CAP:
        cap_do[i.last_sprint] += 1
    all_do[i.last_sprint] += 1

grid_say = default_int_dict()
cap_say = default_int_dict()
all_say = default_int_dict()

for i in lst2:
    team = labels_2_team(i.labels)
    first_sprint = resolve_first_sprint(i.created_at)
    if team == TeamEnum.UNDEFINED:
        continue
    if team == TeamEnum.ADI:
        continue
    if team == TeamEnum.GRID:
        grid_say[first_sprint] += 1
    if team == TeamEnum.CAP:
        cap_say[first_sprint] += 1
    all_say[first_sprint] += 1

grid_say_do = default_float_dict()
cap_say_do = default_float_dict()
all_say_do = default_float_dict()

for k in grid_say.keys():
    grid_say_do[k] = grid_do[k] / grid_say[k] * 100
for k in cap_say.keys():
    cap_say_do[k] = cap_do[k] / cap_say[k] * 100
for k in all_say.keys():
    all_say_do[k] = all_do[k] / all_say[k] * 100

grid_say_do = sort_dict(remove_keys(grid_say_do, UNUSED_SPRINTS))
cap_say_do = sort_dict(remove_keys(cap_say_do, UNUSED_SPRINTS))
all_say_do = sort_dict(remove_keys(all_say_do, UNUSED_SPRINTS))

plt.style.use('fivethirtyeight')

plt.plot(
    grid_say_do.keys(),
    grid_say_do.values(),
    label="Grid",
    color="blue"
)

plt.plot(
    cap_say_do.keys(),
    cap_say_do.values(),
    label="Cap",
    color="red"
)

# plt.plot(
#     all_say_do.keys(),
#     all_say_do.values(),
#     label="all",
#     color="green"
# )

the_table = plt.table(
    cellText=[[int(x) for x in grid_say_do.values()], [int(x) for x in cap_say_do.values()]],
    rowLabels=["Grid", "Cap"],
    colLabels=list(grid_say_do.keys()),
    loc='bottom'
)
plt.subplots_adjust(left=0.2, bottom=0.2)
the_table.auto_set_font_size(False)
the_table.set_fontsize(8)
plt.xticks([])

# plt.xlabel('Sprints')
plt.ylabel('%')
plt.title('Say Do')
plt.legend()
plt.show()
