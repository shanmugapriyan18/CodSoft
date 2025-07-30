# SIMPLE CALCULATOR

def calculator():
    print("\n--- CALCULATOR ---")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("Choose operation: +  -  *  /")
    operation = input("Enter operation: ")

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Division by zero.")
            return
    else:
        print("Invalid operation.")
        return

    print("Result:", result)

calculator()
