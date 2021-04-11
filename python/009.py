# Name:     Special Pythagorean triplet
# Source:   https://projecteuler.net/problem=9


def get_product_of_triplet(sum_):
    
    for a in range(1, sum_):
        for b in range(a + 1, sum_):
            c = sum_ - a - b

            if a**2 + b**2 == c**2: return a*b*c


print(get_product_of_triplet(1000))
