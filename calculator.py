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
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: enter a number")

def get_operation():
    while True:
        op = input("Operation: ( + , - , * , / , ^, q to quit)")
        if op in ["+", "-", "*", "/", "^", "q"]:
            return op
        print("Error, try again.")

def calculate(a, op, b):
    return operation_dict[op](a, b) 

operation_dict = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
    "^" : power
}

def main():
    history = []
    print("--- CALCULATOR ---")
    while True:
        a = get_number("a =")
        o = get_operation()
        if o == "q":
            break
        b = get_number("b =")
        result = f"Result: {a} {o} {b} = {calculate(a, o, b)}"
        history.append(result)
        print(result)
        print("\n History:")
        for i, v in enumerate(history[-5:]):
            print(f"{i+1}: {v}")

main()
# 
# main()tests
# print(add(2, 3))        # 5
# print(subtract(3, 2))   # 1
# print(multiply(3, 4))   # 12  
# print(divide(16, 2))    # 8
# print(power(3, 3))      # 27