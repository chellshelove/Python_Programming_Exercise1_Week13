def myfibonacci(n):
    # Base cases
    if n == 0:
        return 1
    elif n == 1:
        return 1
    # Recursive case
    else:
        return myfibonacci(n - 1) + myfibonacci(n - 2)

# Example usage
n = 5
print(f"The {n}th Fibonacci number is: {myfibonacci(n)}")