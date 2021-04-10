# Name:     Distinct powers
# Source:   https://projecteuler.net/problem=29


from itertools import product


def distinct_terms(a_max, b_max):

    return len(set(a**b for a, b in product(range(2, a_max + 1), range(2, b_max + 1))))


print(distinct_terms(100, 100))
