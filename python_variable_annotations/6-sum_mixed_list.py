#!/usr/bin/env python3
'''module that return summation of list contian int, float'''
from typing import List, overload


@overload
def sum_mixed_list(mxd_lst: List[int]) -> float:
    '''
    func that return the summation of
    '''
    total = 0.0
    for i in mxd_lst:
        total += i
    return total

@overload
def sum_mixed_list(mxd_lst: List[float]) -> float:
    '''
    func that return the summation of
    '''
    total = 0.0
    for i in mxd_lst:
        total += i
    return total
