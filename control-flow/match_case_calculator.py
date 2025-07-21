num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
ops = int(input("Choose the operation (+, -, *, /): "))
#result = {num1}{ops}{num2}
#print(result)

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
            return
        result = num1 / num2
        op_symbol = '/'
    case _:
        print("Invalid operation selected.")
        return
            
    print(f"{num1} {op_symbol} {num2} = {result}")