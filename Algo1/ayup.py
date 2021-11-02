def binsearch_recursive(target, numbers):
    bottom = 0
    top = len(numbers) - 1 
    mid = round((top + bottom) / 2) 
    if numbers[mid] == target: 
        return mid
    elif numbers[mid] > target:
        return binsearch_recursive(target, numbers[:mid])
    elif numbers[mid] < target: 
        return binsearch_recursive(target, numbers[mid+1:]) + (mid+1)
    

numbers = [1,2,3,4,5,6,9,10,11,12,13,14,15,5333,55555,62467,125462,1395029485,134094698693]
#numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
#numbers = [-1,0,3,5,9,12]
target = 5333

result = binsearch_recursive(target, numbers)

print("Results")
print("Target:", target)
print("Index:", result)
print("Result:", numbers[result])
