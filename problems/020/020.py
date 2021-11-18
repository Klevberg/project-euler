# Name:     Factorial digit sum
# Source:   https://projecteuler.net/problem=20


from math import factorial


sum_of_factorial = lambda num: sum(map(int, str(factorial(num))))


print(sum_of_factorial(100))
