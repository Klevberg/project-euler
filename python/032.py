# Name:     Pandigital products
# Source:   https://projecteuler.net/problem=32


print(sum(set(p for x in range(2, 100) for y in range(111, 5_000) if '0' not in (nums := f'{x}{y}{(p := x*y)}') and len(set(nums)) == len(nums) == 9)))
