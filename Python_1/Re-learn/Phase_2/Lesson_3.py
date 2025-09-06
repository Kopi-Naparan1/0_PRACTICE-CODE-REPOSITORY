
from typing import Tuple, Union

def addition(x: float, y: float):
    return f"{x} + {y} = {x + y:.2f}"

def subtraction(x: float, y: float):
    return f"{x} - {y} = {x - y:.2f}"

def multiplication(x: float, y: float):
    return f"{x} * {y} = {x * y:.2f}"

def division(x: float, y: float):
    return f"{x} / {y} = {x / y:.2f}"

def ask_first_number() -> float:
    while True:
        try:
            first_number = float(input("Input first number: "))
            return first_number
        except ValueError:
            print("Make sure you are typing a number")


def ask_second_number(operation: str) -> float:
    
    while True:
        try:
            second_number = float(input("Input second number: "))

            if operation == "/" and second_number == 0:
                print("Make sure divisor is not 0.")
                continue
            return second_number
        
        except ValueError:
            print("Make sure you are typing a number")

def ask_operation():
    while True:
        operation = input("What operation to use (+,-,*,/)? ").strip()
        if operation in "+_*/":
            return operation

def operation_chooser(operation: str):
    if operation == "+":
        return addition
    elif operation == "-":
        return subtraction
    elif operation == "*":
        return multiplication
    else:
        return division


def calculator():

    choice = ask_operation()

    x = ask_first_number()
    y = ask_second_number(choice)

    operation = operation_chooser(choice)

    print(operation(x, y))

def main():
    calculator()

if __name__ == "__main__":
    main()