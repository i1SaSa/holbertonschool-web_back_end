#!/usr/bin/env python3
"""
module that use Higher-Order Functions
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    the Higher-Order Functions
    """
    def multiplier_func(n: float) -> float:
        return n * multiplier

    return multiplier_func
