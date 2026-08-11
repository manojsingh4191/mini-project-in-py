def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

while True:
    try:
        a = float(input("enter a number: "))
        b = float(input("enter another number: "))
    except ValueError:
        print("Error: Please enter valid numbers")
        continue

    operation = input("enter an operation (+, -, *, /): ")
    if operation == "+":
        print(add(a, b))
    elif operation == "-":
        print(subtract(a, b))
    elif operation == "*":
        print(multiply(a, b))
    elif operation == "/":
        print(divide(a, b))
    else:
        print("Error: Invalid operation")

    loop = input("Do you want to perform another calculation? (yes/no): ")
    if loop.lower() != "yes":
        break
