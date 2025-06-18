def funcThree():
    print("Three")

def funcTwo():
    funcThree()
    print("Two")

def funcOne():
    funcTwo()
    print("One")

# funcOne()

def factorial(n):
    if n == 1:   # Base Case 
        return 1
    return n * factorial(n-1) # Recursive Case

print(factorial(4))