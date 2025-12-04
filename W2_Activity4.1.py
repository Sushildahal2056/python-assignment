#Sushil

class Math_operations:

    def factorial(n):
        if n == 0:
            return 1
        return n * Math_operations.factorial(n - 1)

    def fibonacci_series(n):
        series = []
        for i in range(n):
            series.append(Math_operations.fibonacci(i))
        return series

    def fibonacci(n):
        if n <= 1:
            return n

        return Math_operations.fibonacci(n - 1) + Math_operations.fibonacci(n - 2)
    # As calls reach base cases, results pop back up and combine.


if __name__ == "__main__":
    print("Choose an option:")
    print("1. Factorial")
    print("2. Fibonacci")

    choice = input("Enter choice (1/2): ")
    num= int(input("Enter the number:"))
    if choice == "1":
        ans = Math_operations.factorial(num)
    elif choice == "2":
        ans = Math_operations.fibonacci_series(num)
    else:
        ans = "Invalid choice"

    print("\nFinal result:", ans)