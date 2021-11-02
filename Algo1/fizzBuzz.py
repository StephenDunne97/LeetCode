"""
Multiple of 3, print "Fizz" 
Multiple of 5, print "Buzz" 
Multiples of 3 & 5, print "FizzBuzz"
else, print the number
"""
numbers = list(range(1,101))

for x in numbers:
    if x%3 == 0 and x%5 == 0:
        print("Fizbuzz")
    elif x%3 == 0:
        print("Fizz")
    elif x%5 == 0:
        print("Buzz")
    else: 
        print(x)