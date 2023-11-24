def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

def calculator():
    operations = {
        '1': add,
        '2': subtract,
        '3': multiply,
        '4': divide
    }

    print("Simple Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter choice (1/2/3/4): ")

    if choice in operations:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        result = operations[choice](num1, num2)
        operation_symbol = {'1': '+', '2': '-', '3': '*', '4': '/'}[choice]

        print(f"{num1} {operation_symbol} {num2} = {result}")

    else:
        print("Invalid input. Please enter a valid choice (1/2/3/4).")

calculator()
