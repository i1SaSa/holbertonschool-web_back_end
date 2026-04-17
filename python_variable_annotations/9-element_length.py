#!/usr/bin/env python3
'''module'''
from typing import Callable, Tuple, List


def element_length(lst) -> Callable[[Tuple], List]:
    '''function'''
    return [(i, len(i)) for i in lst]
