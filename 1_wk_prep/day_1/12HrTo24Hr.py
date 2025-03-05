#!/bin/python3

import math
import os
import random
import re
import sys

#
# Convert 12hr clock to 24hr clock time.
# Keep in mind 12AM == 00 && 12PM == 12
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    if (s[:2] == "12"):
        if (s[-2:] == "AM"):
            return("00" + s[2:-2])
        return(s[:-2])    
    elif (s[-2:] == "PM"):
        return(str(int(s[:2])+12) + s[2:-2]) 
    
    return(s[:-2])

if __name__ == '__main__':
    # s = "12:00:00AM"
    # s = "12:00:00PM"
    # s = "07:00:00PM"
    s = "07:00:00AM"

    result = timeConversion(s)

    print(result)

