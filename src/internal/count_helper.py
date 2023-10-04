from src.internal.dict_helper import default_int_dict, remove_keys, sort_dict, default_float_dict, accumulate_data
from src.internal.domain import UNUSED_SPRINTS
from src.internal.enums import TeamEnum
from src.internal.extracted_data import labels_2_team, resolve_first_sprint
from src.internal.math_helper import round_decimals_up


def count_say_do(closed_issues: list, without_epics: list) -> (dict, dict, dict):
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
    for i in without_epics:
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
    for k in all_say_do.keys():
        all_say_do[k] = all_do[k] / all_say[k] * 100

    grid_say_do = sort_dict(remove_keys(grid_say_do, UNUSED_SPRINTS))
    cap_say_do = sort_dict(remove_keys(cap_say_do, UNUSED_SPRINTS))
    all_say_do = sort_dict(remove_keys(all_say_do, UNUSED_SPRINTS))

    return grid_say_do, cap_say_do, all_say_do


def count_velocity(closed_issues: list) -> (dict, dict, dict):
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
    return grid_velocity, cap_velocity, all_velocity


def count_accumulated_backlog(closed_issues: list, all_issues: list) -> (dict, dict, dict, dict, dict, dict):
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
    for i in all_issues:
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

    grid_do_acc = accumulate_data(sort_dict(grid_do))
    grid_say_acc = accumulate_data(sort_dict(grid_say))
    cap_do_acc = accumulate_data(sort_dict(cap_do))
    cap_say_acc = accumulate_data(sort_dict(cap_say))
    all_do_acc = accumulate_data(sort_dict(all_do))
    all_say_acc = accumulate_data(sort_dict(all_say))

    grid_do_acc = remove_keys(grid_do_acc, UNUSED_SPRINTS)
    grid_say_acc = remove_keys(grid_say_acc, UNUSED_SPRINTS)
    cap_do_acc = remove_keys(cap_do_acc, UNUSED_SPRINTS)
    cap_say_acc = remove_keys(cap_say_acc, UNUSED_SPRINTS)
    all_do_acc = remove_keys(all_do_acc, UNUSED_SPRINTS)
    all_say_acc = remove_keys(all_say_acc, UNUSED_SPRINTS)

    return grid_do_acc, grid_say_acc, cap_do_acc, cap_say_acc, all_do_acc, all_say_acc


def count_counter_parts(grid_bugs: list, cap_bugs: list) -> (dict, dict):
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

    return grid_on_cap_acc, cap_on_grid_acc


def count_opened_bugs(bugs: list) -> (dict, dict, dict):
    grid_bugs = default_int_dict()
    cap_bugs = default_int_dict()
    all_bugs = default_int_dict()
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
        all_bugs[first_sprint] += 1

    grid_bugs = sort_dict(remove_keys(grid_bugs, UNUSED_SPRINTS))
    cap_bugs = sort_dict(remove_keys(cap_bugs, UNUSED_SPRINTS))
    all_bugs = sort_dict(remove_keys(all_bugs, UNUSED_SPRINTS))

    return grid_bugs, cap_bugs, all_bugs


def count_bugs_by_adi(adi_bugs: list) -> (dict, dict, dict):
    grid_bugs = default_int_dict()
    cap_bugs = default_int_dict()
    all_bugs = default_int_dict()
    for i in adi_bugs:
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
        all_bugs[first_sprint] += 1
    grid_bugs_by_adi = sort_dict(remove_keys(grid_bugs, UNUSED_SPRINTS))
    cap_bugs_by_adi = sort_dict(remove_keys(cap_bugs, UNUSED_SPRINTS))
    all_bugs_by_adi = sort_dict(remove_keys(all_bugs, UNUSED_SPRINTS))
    return grid_bugs_by_adi, cap_bugs_by_adi, all_bugs_by_adi


def count_defects_ratio(adi_grid_bugs: list, adi_cap_bugs: list, closed_issues: list) -> (dict, dict, dict):
    grid_missed_bugs = default_int_dict()
    cap_missed_bugs = default_int_dict()
    all_missed_bugs = default_int_dict()
    for i in adi_cap_bugs:
        team = labels_2_team(i.labels)
        first_sprint = resolve_first_sprint(i.created_at)
        if team == TeamEnum.GRID:
            grid_missed_bugs[first_sprint] += 1
            all_missed_bugs[first_sprint] += 1
    for i in adi_grid_bugs:
        team = labels_2_team(i.labels)
        first_sprint = resolve_first_sprint(i.created_at)
        if team == TeamEnum.CAP:
            cap_missed_bugs[first_sprint] += 1
            all_missed_bugs[first_sprint] += 1

    grid_missed_acc = accumulate_data(sort_dict(grid_missed_bugs))
    cap_missed_acc = accumulate_data(sort_dict(cap_missed_bugs))
    all_missed_acc = accumulate_data(sort_dict(all_missed_bugs))

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

    grid_do_acc = accumulate_data(sort_dict(grid_do))
    cap_do_acc = accumulate_data(sort_dict(cap_do))
    all_do_acc = accumulate_data(sort_dict(all_do))

    grid_ratio = default_float_dict()
    cap_ratio = default_float_dict()
    all_ratio = default_float_dict()
    for s in grid_missed_acc.keys():
        grid_ratio[s] = round_decimals_up(grid_missed_acc[s] / grid_do_acc[s] * 100)
    for s in cap_missed_acc.keys():
        cap_ratio[s] = round_decimals_up(cap_missed_acc[s] / cap_do_acc[s] * 100)
    for s in cap_missed_acc.keys():
        all_ratio[s] = round_decimals_up(all_missed_acc[s] / all_do_acc[s] * 100)

    grid_ratio = remove_keys(grid_ratio, UNUSED_SPRINTS)
    cap_ratio = remove_keys(cap_ratio, UNUSED_SPRINTS)
    all_ratio = remove_keys(all_ratio, UNUSED_SPRINTS)

    return grid_ratio, cap_ratio, all_ratio
