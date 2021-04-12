# Name:     Sum square difference
# Source:   https://projecteuler.net/problem=6


sum_square_diff = lambda num: sum(range(1, num + 1))**2 - sum(n**2 for n in range(1, num + 1))


print(sum_square_diff(100))
