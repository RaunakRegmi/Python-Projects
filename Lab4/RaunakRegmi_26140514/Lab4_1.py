def add(num1, num2):
    result = 0

    result = num1 + num2

    return result


def subtract(num1, num2):
    result = 0

    result = num1 - num2

    return result


def multiply(num1, num2):
    result = 0

    result = num1 * num2

    return result


def divide(num1, num2):
    if num2 == 0:
        error_message = "Error: Cannot divide by zero!"
        return error_message
    else:
        result = 0
        result = num1 / num2
        return result


def calculator():
    print("Welcome to my calculator!")

    first_number_input = input("Enter number 1: ")
    first_number = float(first_number_input)

    second_number_input = input("Enter number 2: ")
    second_number = float(second_number_input)

    operation = input("Enter operator (* for multiplication, - for subtraction, + for addition, / for division): ")

    answer = 0

    operation_name = ""

    if operation == "+":
        answer = add(first_number, second_number)
        operation_name = "adding"

    elif operation == "-":
        answer = subtract(first_number, second_number)
        operation_name = "subtracting"

    elif operation == "*":
        answer = multiply(first_number, second_number)
        operation_name = "multiplying"

    elif operation == "/":
        answer = divide(first_number, second_number)
        operation_name = "dividing"

    else:
        print("Invalid operator! Please use +, -, * or /")
        return

    print(operation_name, first_number, "by", second_number, "=", answer)

if __name__ == "__main__":
    calculator()
