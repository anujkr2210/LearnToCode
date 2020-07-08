from functools import lru_cache

from Number_validator import validate

# fibonnaci function to calculate the nth value using memorization as this is more efficient
@lru_cache(maxsize=None)
def fibonacci_optimised(num):
    if validate(num):
        no_series = int(num)
        if no_series < 1:
            return ValueError("Value is less than 1. Please enter a value greater than 1")

        # First Fibonacci number is 0
        elif no_series == 1:
            return 0
        # Second Fibonacci number is 1
        elif no_series == 2:
            return 1
        else:
            return fibonacci_optimised(no_series - 1) + fibonacci_optimised(no_series - 2)
    else:
        return "User Input is invalid"

# common implementation of fibonnaci series using recursion
def fibonacci(num):
    if validate(num):
        no_series = int(num)
        if no_series < 1:
            return ValueError("Value is less than 1. Please enter a value greater than 1")

        # First Fibonacci number is 0
        elif no_series == 1:
            return 0
        # Second Fibonacci number is 1
        elif no_series == 2:
            return 1
        else:
            return fibonacci(no_series - 1) + fibonacci(no_series - 2)
    else:
        return "User Input is invalid"
