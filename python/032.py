# Name:     Pandigital products
# Source:   https://projecteuler.net/problem=32


from itertools import product


def pandigital_products_sum():

    pd_products = set(p for x, y in product(range(2, 100), range(111, 5_000)) if '0' not in (nums := f'{x}{y}{(p := x*y)}') and len(set(nums)) == len(nums) == 9)
    
    return sum(pd_products)


print(pandigital_products_sum())
