num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

match operation:
    case '+':
        result = num1 + num2
        op_symbol = '+'
    case '-':
        result = num1 - num2
        op_symbol = '-'
    case '*':
        result = num1 * num2
        op_symbol = '*'
    case '/':
        if num2 == 0:
            print("Error: Division by zero is undefined.")
            exit()
        result = num1 / num2
        op_symbol = '/'
    case _:
        print("Invalid operation selected.")
        exit()

print(f"{num1} {op_symbol} {num2} = {result}")
