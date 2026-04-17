#!/usr/bin/env python3
'''module'''
from typing import Tuple, List, Sequence, Iterable


def element_length(lst: Iterable) -> List[Tuple[Sequence, int]]:
    '''function'''
    return [(i, len(i)) for i in lst]
