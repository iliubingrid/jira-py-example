import matplotlib.pyplot as plt

from src.internal.csv_helper import read_from_csv_file
from src.internal.dict_helper import sort_dict, default_int_dict, accumulate_data, remove_keys
from src.internal.domain import UNUSED_SPRINTS
from src.internal.enums import TeamEnum
from src.internal.extracted_data import labels_2_team, resolve_first_sprint

lst = read_from_csv_file("tmp/list.csv")

closed_issues = list(filter(lambda x: (x.status == "Done"), lst))

grid_do = default_int_dict()
cap_do = default_int_dict()
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

grid_say = default_int_dict()
cap_say = default_int_dict()
for i in lst:
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

# grid_do_acc = accumulate_data(sort_dict(grid_do))
# grid_say_acc = accumulate_data(sort_dict(grid_say))
# cap_do_acc = accumulate_data(sort_dict(cap_do))
# cap_say_acc = accumulate_data(sort_dict(cap_say))

grid_do_acc = accumulate_data(sort_dict(remove_keys(grid_do, UNUSED_SPRINTS)))
grid_say_acc = accumulate_data(sort_dict(remove_keys(grid_say, UNUSED_SPRINTS)))
cap_do_acc = accumulate_data(sort_dict(remove_keys(cap_do, UNUSED_SPRINTS)))
cap_say_acc = accumulate_data(sort_dict(remove_keys(cap_say, UNUSED_SPRINTS)))

grid_do_acc = remove_keys(grid_do_acc, UNUSED_SPRINTS)
grid_say_acc = remove_keys(grid_say_acc, UNUSED_SPRINTS)
cap_do_acc = remove_keys(cap_do_acc, UNUSED_SPRINTS)
cap_say_acc = remove_keys(cap_say_acc, UNUSED_SPRINTS)

plt.style.use('fivethirtyeight')

plt.plot(
    grid_say_acc.keys(),
    grid_say_acc.values(),
    label="Grid Opened",
    color="blue"
)
plt.plot(
    grid_do_acc.keys(),
    grid_do_acc.values(),
    label="Grid Resolved",
    color="orange"
)
plt.plot(
    cap_say_acc.keys(),
    cap_say_acc.values(),
    label="Cap Opened",
    color="red"
)
plt.plot(
    cap_do_acc.keys(),
    cap_do_acc.values(),
    label="Cap Resolved",
    color="green"
)

the_table = plt.table(
    cellText=[
        list(grid_say_acc.values()),
        list(grid_do_acc.values()),
        list(cap_say_acc.values()),
        list(cap_do_acc.values())],
    rowLabels=["Grid Opened", "Grid Resolved", "Cap Opened", "Cap Resolved"],
    colLabels=list(grid_say_acc.keys()),
    loc='bottom'
)
plt.subplots_adjust(left=0.2, bottom=0.2)
the_table.auto_set_font_size(False)
the_table.set_fontsize(8)
plt.xticks([])

# plt.xlabel('Sprints')
plt.ylabel('Issues')
plt.title('Accumulated Created vs Resolved')
plt.legend()
plt.show()
