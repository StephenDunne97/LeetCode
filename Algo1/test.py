"""
3 methods:
1. insert()
2. [] +
3. Slicing
"""

def listtoint(passedlist):
    res = []
    for x in passedlist: # Returns [4, 3, 2, 1]
        res[:0] = [x]
    res = int("".join(map(str,res))) # Returns 4321
    return res

def inttolist(number):
    res = []
    res[:0]=str(number)
    return res

numArr1 = [4,2]
numArr2 = [6,1]

num1 = listtoint(numArr1)
num2 = listtoint(numArr2)
result = num1+num2
result = inttolist(result)
print(result)
