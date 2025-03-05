#!/bin/python3

#
# Calculate + Print the ratio of plus/minus/zero numbers in an integer array
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    pos=0
    neg=0
    zero=0
    
    for x in arr:
        if (x>0):
            pos+=1
        elif(x<0):
            neg+=1
        else:
            zero+=1
    
    print("%.6f" % float(pos/len(arr)))
    print("%.6f" % float(neg/len(arr)))
    print("%.6f" % float(zero/len(arr)))
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
