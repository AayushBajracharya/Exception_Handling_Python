try:
    int(input("Enter a number: ")) 
    result = 10 / 0
except Exception as e:
    print(f"Unexpected error: {e}")
