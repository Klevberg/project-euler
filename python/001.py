# Name:     Multiples of 3 and 5
# Source:   https://projecteuler.net/problem=1


def sum_of_multiples(num_below, *nums_multiple):

    return sum(set(n for n in range(num_below) for num in nums_multiple if n % num == 0))


print(sum_of_multiples(1000, 3, 5))
