# Name:     Even Fibonacci numbers
# Source:   https://projecteuler.net/problem=2

def even_fibonacci_sum(num_below):

    num_1, num_2 = 1, 2
    n = 0

    even_fib = [2] if 2 < num_below else []

    while n < num_below:
        n = num_1 + num_2

        if n % 2 == 0:
            even_fib.append(n)
        
        num_1, num_2 = num_2, n
    
    return sum(even_fib)


print(even_fibonacci_sum(4_000_000))