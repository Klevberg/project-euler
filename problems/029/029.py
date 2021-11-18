# Name:     Distinct powers
# Source:   https://projecteuler.net/problem=29



distinct_terms = lambda a_max, b_max: len({a**b for a in range(2, a_max + 1) for b in range(2, b_max + 1)})


print(distinct_terms(100, 100))
