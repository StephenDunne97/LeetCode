#!/bin/python3

import math
import os
import random
import re
import sys

#
# Calc and print the value of the 4 lowest and 4 highest values in a 5 digit array
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    total = sum(arr)
    print(total-max(arr), total-min(arr))

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
