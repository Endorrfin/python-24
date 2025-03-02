import art


def add(n1, n2):
    return n1 + n2

# TODO: Write out the other 3 function - subtract, multiply and divide
def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# TODO: Add these 4 function into a dictionary as the values. Keys = '+', '-', '*', '/'

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}


# TODO: Use the dictionary operations to perform the calculations. Multiply 4 * 8 using the dictionary
# print(operations["*"](4, 8))

def calculator():
    print(art.logo)
    should_accumulate = True
    num1 = float(input("What is the first number?: "))

    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What is the next number?: "))
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to cancel:")

        if choice == 'y':
            num1 = answer
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()

calculator()