"""
Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
"""

def two_sum(arr, target):
    target_acquired = False
    pos_x = 1
    pos_y = 1
    result = []
    for x in arr:
        if target_acquired == True:
            break
        elif x > target:
            pos_x+=1
            continue
        pos_y = 1 
        for y in arr:
            if y > target or pos_y == pos_x:
                pos_y+=1
                continue
            elif x + y == target:
                print("X:", x, "Y:", y)
                result.append(pos_x-1)
                result.append(pos_y-1)
                target_acquired = True
                return(result)
            pos_y+=1
        pos_x +=1

def main():
    arr = [2,2,11,47,1,500,2,44,55,42,442,1234,74,2]
    target = 4
    result = two_sum(arr,target)
    print(result)
if __name__ == "__main__":
    main()


