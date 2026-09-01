
def calculator():

    a = int(input("enter the first number: "))
    operator = input("enter the operation: ")
    b = int(input("enter the second number: "))
    match operator:
        case '+':
            result = a + b
            print(f"Result: {result}")
        case '-':
            result = a - b
            print(f"Result: {result}")
        case '*': 
            result = a * b
            print(f"Result: {result}")
        case '/':
            result = a / b
            print(f"Result: {result}")
        case _:
            print("invalid operator entered")

calculator()
