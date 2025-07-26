def perform_operation(num1: float, num2: float, operation: str):
    """
    Perform an arithmetic operation on two numbers.

    Parameters:
    - num1 (float): First number
    - num2 (float): Second number
    - operation (str): One of 'add', 'subtract', 'multiply', or 'divide'

    Returns:
    - float or str: Result of the operation or error message for division by zero
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "ERROR: Division by zero"
        return num1 / num2
    else:
        return "ERROR: Invalid operation"
