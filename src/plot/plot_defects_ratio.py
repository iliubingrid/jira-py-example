import matplotlib.pyplot as plt

from src.internal.csv_helper import read_from_csv_file
from src.internal.dict_helper import sort_dict, default_int_dict, remove_keys, accumulate_data, default_float_dict
from src.internal.domain import UNUSED_SPRINTS
from src.internal.enums import TeamEnum
from src.internal.extracted_data import resolve_first_sprint, labels_2_team
from src.internal.math_helper import round_decimals_up

lst = read_from_csv_file("tmp/list.csv")

closed_issues = list(filter(lambda x: (x.status == "Done"), lst))
adi_cap_bugs = list(filter(lambda x: (x.issue_type == "Bug" and x.reporter_team in [TeamEnum.CAP, TeamEnum.ADI]), lst))
adi_grid_raised_bugs = list(filter(lambda x: (x.issue_type == "Bug" and x.reporter_team in [TeamEnum.GRID, TeamEnum.ADI]), lst))

grid_missed_bugs = default_int_dict()
for i in adi_cap_bugs:
    team = labels_2_team(i.labels)
    first_sprint = resolve_first_sprint(i.created_at)
    if team == TeamEnum.GRID:
        grid_missed_bugs[first_sprint] += 1
cap_missed_bugs = default_int_dict()
for i in adi_grid_raised_bugs:
    team = labels_2_team(i.labels)
    first_sprint = resolve_first_sprint(i.created_at)
    if team == TeamEnum.CAP:
        cap_missed_bugs[first_sprint] += 1

grid_missed_acc = accumulate_data(sort_dict(grid_missed_bugs))
cap_missed_acc = accumulate_data(sort_dict(cap_missed_bugs))

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

grid_do_acc = accumulate_data(sort_dict(grid_do))
cap_do_acc = accumulate_data(sort_dict(cap_do))

grid_ratio = default_float_dict()
cap_ratio = default_float_dict()
for s in grid_missed_acc.keys():
    grid_ratio[s] = round_decimals_up(grid_missed_acc[s] / grid_do_acc[s] * 100)
for s in cap_missed_acc.keys():
    cap_ratio[s] = round_decimals_up(cap_missed_acc[s] / cap_do_acc[s] * 100)

grid_ratio = remove_keys(grid_ratio, UNUSED_SPRINTS)
cap_ratio = remove_keys(cap_ratio, UNUSED_SPRINTS)

plt.style.use('fivethirtyeight')

plt.plot(
    grid_ratio.keys(),
    grid_ratio.values(),
    label="Grid",
    color="blue"
)
plt.plot(
    cap_ratio.keys(),
    cap_ratio.values(),
    label="Cap",
    color="red"
)

the_table = plt.table(
    cellText=[list(grid_ratio.values()), list(cap_ratio.values())],
    rowLabels=["Grid", "Cap"],
    colLabels=list(grid_ratio.keys()),
    loc='bottom'
)
plt.subplots_adjust(left=0.2, bottom=0.2)
the_table.auto_set_font_size(False)
the_table.set_fontsize(8)
plt.xticks([])

# plt.xlabel('Sprints')
plt.ylabel('Issues')
plt.title('Defects Ratio')
plt.legend()
plt.show()
