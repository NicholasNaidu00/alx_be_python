# robust_division_calculator.py

def safe_divide(numerator, denominator):
    try:
        # Attempt to convert inputs to floats
        numerator = float(numerator)
        denominator = float(denominator)

        # Attempt to perform the division
        result = numerator / denominator
        return f"The result is: {result}"
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except ValueError:
        return "Error: Non-numeric input provided. Please enter valid numbers."

if __name__ == "__main__":
    # Example usage for testing
    print(safe_divide(10, 2))
    print(safe_divide(10, 0))
    print(safe_divide('a', 2))
