from typing import Iterable


def to_len(target: Iterable, length: int, default=None):
    target = list(target)
    assert len(target) <= length, 'Target should be shorter than length'
    return target + [default] * (length - len(target))


def to_dict(keys: Iterable, values: Iterable):
    keys = list(keys)
    values = list(values)
    assert len(keys) >= len(values), 'Values should be longer than keys'
    return dict(zip(keys, to_len(values, len(keys))))
