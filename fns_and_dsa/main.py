from arithmetic_operations import perform_operation

def main():
    print("Arithmetic Operations")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()

    result = perform_operation(num1, num2, operation)
    
    if isinstance(result, str) and result.startswith("ERROR"):
        print(f"Operation failed: {result}")
    else:
        print(f"Result: {result}")

if __name__ == "__main__":
    main()
