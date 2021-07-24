#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from decimal import Decimal

def round_num(n, decimals):
    '''
    Params:
    n - number to round
    decimals - number of decimal places to round to
    Round number to 2 decimal places
    For example:
    10.0 -> 10
    10.222 -> 10.22
    '''
    return n.to_integral() if n == n.to_integral() else round(n.normalize(), decimals)

def drop_zero(n):
    '''
    Drop trailing 0s
    For example:
    10.100 -> 10.1
    '''
    n = str(n)
    return n.rstrip('0').rstrip('.') if '.' in n else n

	
def numerize(n, decimals=2):
    '''
    Params:
    n - number to be numerized
    decimals - number of decimal places to round to
    Converts numbers like:
    1,000 -> 1K
    1,000,000 -> 1M
    1,000,000,000 -> 1B
    1,000,000,000,000 -> 1T
    '''
    is_negative_string = ""
    if n < 0:
        is_negative_string = "-"
    n = abs(Decimal(n))
    if n < 1000:
        return is_negative_string + str(drop_zero(round_num(n, decimals)))
    elif n >= 1000000000000000:
        return is_negative_string + str(n)
    counter = -1
    num = ["K", "M", "B", "T"]
    while n >= 1000:
        if counter + 1 > 3:
            break
        n /= 1000
        counter += 1
    return is_negative_string + str(n) + num[counter]
  
if __name__ == '__main__':
    num = numerize(1000)
    print(f"The result is {num}")
