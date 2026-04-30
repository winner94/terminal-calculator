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

def get_number(prompt):
    try:
        return float(input(prompt))
    except ValueError:
        print("Error: enter a number")
        return None

def get_operation():
    op = input("Operation: ( + , - , * , / , ^)")
    if op not in ["+", "-", "*", "/", "^"]:
        print("Error: unknown operation")
        return None
    return op

def calculate(a, op, b):
    return operation_dict[op](a, b) 

operation_dict = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
    "^" : power
}

a = get_number("a =")
o = get_operation()
b = get_number("b =")
print(calculate(a, o, b))


# tests
print(add(2, 3))        # 5
print(subtract(3, 2))   # 1
print(multiply(3, 4))   # 12  
print(divide(16, 2))    # 8
print(power(3, 3))      # 27