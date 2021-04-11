# Name:     Distinct powers
# Source:   https://projecteuler.net/problem=29


def distinct_terms(a_max, b_max):

    return len(set(a**b for a in range(2, a_max + 1) for b in range(2, b_max + 1)))


print(distinct_terms(100, 100))
