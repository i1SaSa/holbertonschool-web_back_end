#!/usr/bin/env python3
""" module that return summation of list contian int, float """
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ func that return the summation of a list of floats and ints """
    return float(sum(mxd_lst))
