#!/usr/bin/env python3
'''module return summation of a list'''


def sum_list(input_list: list[float]) -> float:
    ''' 
    take a list and return their sum
    @input_list: the list
      '''
    total = 0
    for i in input_list:
        total += i
    return total
