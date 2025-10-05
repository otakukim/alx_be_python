def safe_divide(numerator, denominator):
    """
    Performs division of numerator by denominator with robust error handling.
    
    Args:
        numerator: The numerator, expected to be numeric (int or float).
        denominator: The denominator, expected to be numeric (int or float).
    
    Returns:
        A string with either the result of the division or an appropriate error message.
    """
    # Convert inputs to float
    try:
        num = float(numerator)
        denom = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."
    
    # Attempt division
    try:
        result = num / denom
        return f"The result of the division is {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
import sys
from robust_division_calculator import safe_divide

def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)

    numerator = sys.argv[1]
    denominator = sys.argv[2]

    result = safe_divide(numerator, denominator)
    print(result)

if __name__ == "__main__":
    main()

