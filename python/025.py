# Name:     1000-digit Fibonacci number
# Source:   https://projecteuler.net/problem=25


def fibonacci(digits):
    
    a, b, n = 1, 1, 0
    counter = 2

    while len(str(n)) < digits:
        n = a + b
        a, b = b, n
        counter += 1

    return counter if digits != 1 else 1


print(fibonacci(1000))
