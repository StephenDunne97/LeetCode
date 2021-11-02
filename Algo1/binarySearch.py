from timeit import default_timer as timer

def binsearch_iterative(target, bottom, top, mid, numbers):
    found = False

    while found == False:
        if numbers[mid] == target: 
            return mid
        elif numbers[bottom] == target:
            return bottom
        elif numbers[top] == target:
            return top
        elif numbers[mid] > target:
            top = mid - 1
            mid = (top + bottom) // 2
        elif numbers[mid] < target:    
            bottom = mid + 1
            mid = (top + bottom) // 2

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
bottom = 0
top = len(numbers) - 1 
mid = round((top + bottom) / 2)
target = 5333

print("Iterative Binary Search Results:")
print("=============")
start = timer()
result = binsearch_iterative(target, bottom, top, mid, numbers)
end = timer()
print("Target:", target)
print("Index:", result)
print("Result:", numbers[result])
print("Time:", end-start)

print("Recusive Binary Search Results:")
print("=============")
start = timer()
result = binsearch_recursive(target, numbers)
end = timer()
print("Target:", target)
print("Index:", result)
print("Result:", numbers[result])
print("Time:", end-start)