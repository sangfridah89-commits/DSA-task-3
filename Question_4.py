#Question a
def sum_natural(n):
    if n == 0:
        return 0
    else:
        return n + sum_natural(n - 1)


number = int(input("Enter a number: "))

result = sum_natural(number)

print("Sum of natural numbers:", result)
#Question b

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


number = int(input("Enter a number: "))

if number < 0:
    print("Factorial is not defined for negative numbers")
else:
    print("Factorial:", factorial(number))
#Question c

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


number = int(input("Enter the term number: "))

if number < 0:
    print("Enter a non-negative number")
else:
    print("Fibonacci term:", fibonacci(number))
#Question d

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


number = int(input("Enter the number of terms: "))

if number < 0:
    print("Enter a non-negative number")
else:
    print("Fibonacci series:")

    for i in range(number):
        print(fibonacci(i), end=" ")


