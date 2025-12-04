def fibonacci(n):
    if n<=0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def fibonacci_series(n):
    series=[]
    for i in range(n):
        series.append(fibonacci(i))
    return series

def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

def main():
    num= int(input("Enter a number:"))
    fib= fibonacci_series(num)
    fact= factorial(num)
    print("The factorial of",num,"is",fact)
    print("The fibonacci of",num,"is",fib)

if __name__ == "__main__":
    main()