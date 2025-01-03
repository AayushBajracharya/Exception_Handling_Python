class CustomError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def divide(a, b):
    if b == 0:
        raise CustomError("Division by zero is not allowed.")
    return a / b

try:
    x = int(input("Enter a Number1: "))
    y = int(input("Enter a Number2: "))

    result = divide(x, y)
    print(f"Division is: {result}")
    
except CustomError as e:
    		print(f"CustomError: {e}")