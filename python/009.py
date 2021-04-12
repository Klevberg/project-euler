# Name:     Special Pythagorean triplet
# Source:   https://projecteuler.net/problem=9


product_of_triplet = lambda sum_: next(a*b*c for a in range(1, sum_) for b in range(a + 1, sum_) if a**2 + b**2 == (c := sum_ - a - b)**2)


print(product_of_triplet(1000))
