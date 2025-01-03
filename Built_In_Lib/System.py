# import sys

# # Get the version of Python
# python_version = sys.version
# print(f"Python Version: {python_version}")

# # Get the list of command-line arguments
# command_line_args = sys.argv
# print(f"Command Line Arguments: {command_line_args}")

# # Exit from Python
# print("Exiting...")
# sys.exit()


import sys

def main():
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage: python System.py <num1> <num2> <operation>")
        print("Example: python System.py 10 5 add")
        return

    # Extract arguments
    num1 = float(sys.argv[1])  # First number
    num2 = float(sys.argv[2])  # Second number
    operation = sys.argv[3].lower()  # Operation (convert to lowercase)

    # Perform the specified operation
    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            return
        result = num1 / num2
    else:
        print(f"Error: Unknown operation '{operation}'. Supported operations are add, subtract, multiply, divide.")
        return

    # Print the result
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
