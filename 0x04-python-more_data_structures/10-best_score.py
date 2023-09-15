#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    _maxv = 0
    _maxk = 0
    for k, v in a_dictionary.items():
        if v > _maxv:
            _maxk = k
            _maxv = v
    return _maxk
