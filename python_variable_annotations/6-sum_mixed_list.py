#!/usr/bin/env python3
'''module that return summation of list contian int, float'''
from typing import List


def sum_mixed_list(mxd_lst: List[float | int]) -> float:
    '''
    func that return the summation of
    '''
    total = 0.0
    for i in mxd_lst:
        total += i
    return total
