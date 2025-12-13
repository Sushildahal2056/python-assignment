class MathSeries:
    """
    This class stores a number (n) and provides two features:
    1. Generate the entire Fibonacci series up to n terms.
    2. Compute factorial using recursion.
    """

    def __init__(self, n):
        """
        __init__ is the constructor.
        It runs automatically when you create an object of this class.

        Whatever number you give while creating the object will
        be stored in self.n for later use.
        """
        self.n = n

    def factorial_recursive(self, n=None):
        """
        Recursive factorial function.
        If n is not provided, use the object's number (self.n).
        """
        if n is None:
            n = self.n

        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers.")

        # Base cases: factorial of 0 and 1 is 1
        if n in (0, 1):
            return 1

        # Recursive case: n * factorial of (n-1)
        return n * self.factorial_recursive(n - 1)

    def fibonacci_series(self):
        """
        Generate full Fibonacci series up to n terms.

        This version is NOT recursive because recursion is slow for series.
        """
        n = self.n

        # If user enters 0 or negative, return empty list
        if n <= 0:
            return []

        # If user wants only first term
        if n == 1:
            return [0]

        # Start with the first two Fibonacci numbers
        series = [0, 1]

        # Loop to build the rest of the series
        for i in range(2, n):
            next_number = series[-1] + series[-2]  # last two numbers
            series.append(next_number)

        return series


# ---------------- MAIN PROGRAM ----------------
if __name__ == "__main__":
    # Ask user the number of terms
    n = int(input("Enter how many Fibonacci numbers you want: "))

    # Create an object of MathSeries class
    """
    Example:
        If n = 5
        obj = MathSeries(5)

    Now obj.n = 5
    And every method of obj can use this number.
    """
    obj = MathSeries(n)

    # Print the full Fibonacci series
    print("\nFull Fibonacci Series:")
    print(obj.fibonacci_series())

    # Print factorial using recursion
    print(f"\nFactorial of {n}:")
    print(obj.factorial_recursive())

