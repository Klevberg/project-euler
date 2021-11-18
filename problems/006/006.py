# Name:     Sum square difference
# Source:   https://projecteuler.net/problem=6


num = 100

print(sum(range(1, num + 1))**2 - sum(n**2 for n in range(1, num + 1)))
