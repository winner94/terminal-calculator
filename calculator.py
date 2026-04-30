def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: cannot divide by 0"
    return a / b

def power(a, b):
    return pow(a,b)


# tests
print(add(2, 3))        # 5
print(subtract(3, 2))   # 1
print(multiply(3, 4))   # 12  
print(divide(16, 2))    # 8
print(power(3, 3))      # 27