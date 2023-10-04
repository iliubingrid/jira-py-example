import matplotlib.pyplot as plt

from src.internal.csv_helper import read_from_csv_file
from src.internal.dict_helper import sort_dict, default_int_dict, remove_keys
from src.internal.domain import UNUSED_SPRINTS
from src.internal.enums import TeamEnum
from src.internal.extracted_data import labels_2_team

lst = read_from_csv_file("tmp/list.csv")

lst2 = list(filter(lambda x: (x.issue_type != "Epic"), lst))
closed_issues = list(filter(lambda x: (x.status == "Done"), lst2))

grid_velocity = default_int_dict()
cap_velocity = default_int_dict()
all_velocity = default_int_dict()
for i in closed_issues:
    team = labels_2_team(i.labels)
    if team == TeamEnum.UNDEFINED:
        continue
    if team == TeamEnum.ADI:
        continue
    if team == TeamEnum.GRID:
        grid_velocity[i.last_sprint] += 1
    if team == TeamEnum.CAP:
        cap_velocity[i.last_sprint] += 1
    all_velocity[i.last_sprint] += 1

grid_velocity = sort_dict(remove_keys(grid_velocity, UNUSED_SPRINTS))
cap_velocity = sort_dict(remove_keys(cap_velocity, UNUSED_SPRINTS))
all_velocity = sort_dict(remove_keys(all_velocity, UNUSED_SPRINTS))

plt.style.use('fivethirtyeight')

plt.plot(
    grid_velocity.keys(),
    grid_velocity.values(),
    label="Grid",
    color="blue"
)

plt.plot(
    cap_velocity.keys(),
    cap_velocity.values(),
    label="Cap",
    color="red"
)

# plt.plot(
#     all_velocity.keys(),
#     all_velocity.values(),
#     label="all",
#     color="green"
# )

the_table = plt.table(
    cellText=[list(grid_velocity.values()), list(cap_velocity.values())],
    rowLabels=["Grid", "Cap"],
    colLabels=list(grid_velocity.keys()),
    loc='bottom'
)
plt.subplots_adjust(left=0.2, bottom=0.2)
the_table.auto_set_font_size(False)
the_table.set_fontsize(8)
plt.xticks([])
# plt.xlabel('Sprints')

plt.ylabel('Resolved Issues')
plt.title('Velocity')
plt.legend()
plt.show()
