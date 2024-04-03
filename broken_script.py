def add_numbers(num1, num2):
    # Broken: Attempts to add without ensuring type compatibility
    return num1 + num2

def multiply_numbers(num1, num2):
    # Broken: Wrong operation is performed
    return num1 - num2  # This should be a multiplication operation

# Main execution with bugs
if __name__ == "__main__":
    result = add_numbers(10, '20')  # This will cause a TypeError
    print(f"The addition result is: {result}")

    result = multiply_numbers(10, 5)  # This will give an incorrect result
    print(f"The multiplication result is: {result}")
