# Uncaught exception from your code
def divide_numbers(a, b):
    return a / b

# Caught exception from your code
def divide_by_zero_with_error_handling():
    try:
        result = 10 / 0  # Raises a ZeroDivisionError (caught)
    except ZeroDivisionError:
        print("Caught a ZeroDivisionError ")

#divide_numbers(5, 0)  # Raises a ZeroDivisionError
divide_by_zero_with_error_handling
