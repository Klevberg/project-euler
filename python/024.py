# Name:     Lexicographic permutations
# Source:   https://projecteuler.net/problem=24


from itertools import permutations


get_permutation = lambda digits, nth_permutation: int(''.join(map(str, list(permutations(digits))[nth_permutation - 1])))


print(get_permutation(range(10), 1_000_000))
