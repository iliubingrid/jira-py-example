from collections import defaultdict

from src.internal.domain import SPRINTS


def sort_dict(d: dict) -> dict:
    return dict(sorted(d.items()))


def default_int_dict() -> dict:
    d = defaultdict(int)
    for s in SPRINTS:
        d[s] = 0
    return d


def default_float_dict() -> dict:
    d = defaultdict(float)
    for s in SPRINTS:
        d[s] = 0
    return d


def remove_keys(d: dict, keys: list) -> dict:
    for k in keys:
        d.pop(k, None)
    return d


def accumulate_data(d: dict) -> dict:
    new_d = default_int_dict()
    prev = 0
    for k in d.keys():
        prev += d[k]
        new_d[k] = prev
    return new_d
