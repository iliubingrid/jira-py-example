from src.internal.count_helper import (count_accumulated_backlog,
                                       count_bugs_by_adi, count_counter_parts,
                                       count_defects_ratio, count_opened_bugs,
                                       count_say_do, count_velocity)
from src.internal.csv_helper import read_from_csv_file
from src.internal.enums import TeamEnum
from src.internal.plot_helper import (accumulated_backlog_to_html,
                                      bugs_by_adi_to_html, bugs_ratio_to_html,
                                      counter_parts_to_html,
                                      opened_bugs_to_html, say_do_to_html,
                                      velocity_to_html)

lst = read_from_csv_file("tmp/list.csv")

without_epics = list(filter(lambda x: (x.issue_type != "Epic"), lst))
closed_issues_without_epics = list(filter(lambda x: (x.status == "Done"), without_epics))
closed_issues = list(filter(lambda x: (x.status == "Done"), lst))
bugs = list(filter(lambda x: (x.issue_type == "Bug"), lst))
adi_bugs = list(filter(lambda x: (x.issue_type == "Bug" and x.reporter_team == TeamEnum.ADI), lst))
cap_bugs = list(filter(lambda x: (x.issue_type == "Bug" and x.reporter_team == TeamEnum.CAP), lst))
grid_bugs = list(filter(lambda x: (x.issue_type == "Bug" and x.reporter_team == TeamEnum.GRID), lst))
adi_cap_bugs = list(filter(lambda x: (x.issue_type == "Bug" and x.reporter_team in [TeamEnum.CAP, TeamEnum.ADI]), lst))
adi_grid_bugs = list(filter(lambda x: (x.issue_type == "Bug" and x.reporter_team in [TeamEnum.GRID, TeamEnum.ADI]), lst))

grid_say_do, cap_say_do, all_say_do = count_say_do(closed_issues_without_epics, without_epics)
grid_velocity, cap_velocity, all_velocity = count_velocity(closed_issues_without_epics)
grid_do_acc, grid_say_acc, cap_do_acc, cap_say_acc, all_do_acc, all_say_acc = count_accumulated_backlog(closed_issues, lst)
grid_bugs_by_adi, cap_bugs_by_adi, all_bugs_by_adi = count_bugs_by_adi(adi_bugs)
grid_on_cap_acc, cap_on_grid_acc = count_counter_parts(grid_bugs, cap_bugs)
grid_bugs, cap_bugs, all_bugs = count_opened_bugs(bugs)
grid_defects_ratio, cap_defects_ratio, all_defects_ratio = count_defects_ratio(adi_grid_bugs, adi_cap_bugs, closed_issues)

say_do_plot = say_do_to_html(grid_say_do, cap_say_do, all_say_do)
velocity_plot = velocity_to_html(grid_velocity, cap_velocity, all_velocity)
accumulated_backlog_plot = accumulated_backlog_to_html(grid_do_acc, grid_say_acc, cap_do_acc, cap_say_acc, all_do_acc, all_say_acc)
opened_bugs_plot = opened_bugs_to_html(grid_bugs, cap_bugs, all_bugs)
bugs_by_adi_plot = bugs_by_adi_to_html(grid_bugs_by_adi, cap_bugs_by_adi, all_bugs_by_adi)
counter_parts_plot = counter_parts_to_html(grid_on_cap_acc, cap_on_grid_acc)
defects_ratio_ratio = bugs_ratio_to_html(grid_defects_ratio, cap_defects_ratio, all_defects_ratio)

html_string = '''
<html>
    <head>
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css">
        <style>body{ margin:0 100; background:white; }</style>
    </head>
    <body>
        <table>
            <tr>
                <td>
                    ''' + say_do_plot + '''
                </td>
                <td>
                    ''' + velocity_plot + '''
                </td>
            </tr>

            <tr>
                <td>
                    ''' + accumulated_backlog_plot + '''
                </td>
                <td>
                    ''' + opened_bugs_plot + '''
                </td>
            </tr>

            <tr>
                <td>
                    ''' + bugs_by_adi_plot + '''
                </td>
                <td>
                    ''' + defects_ratio_ratio + '''
                </td>
            </tr>
        </table>

    </body>
</html>'''

f = open('report.html', 'w')
f.write(html_string)
f.close()
