on = True
def add():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print(f"The sum of {a} and {b} is {a + b}")

def subtract():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print(f"The difference of {a} and {b} is {a - b}")

def multiply():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print(f"The product of {a} and {b} is {a * b}")

def divide():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    if b == 0:
        print("Error: Division by zero is not allowed.")
    else:
        print(f"The quotient of {a} and {b} is {a / b}")

while on:
    operation = input("Please type  +, - , *, / or q: ")
    if operation == "+":
        add()
    elif operation == "-":
        subtract()
    elif operation == "*":
        multiply()
    elif operation == "/":
        divide()
    elif operation == "q":
        print("Exiting the calculator. Goodbye!")
        on = False
    else:
        print("Invalid operation. Please enter +, -, *, / or q.")


