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
    arr.sort()
    highArr = arr[-4:]
    lowArr = arr[:4]
    
    high=0
    low=0
    
    for x in highArr:
        high+=x
        
    for x in lowArr:
        low+=x   
        
    print(low, high) 

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
