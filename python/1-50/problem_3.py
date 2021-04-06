"""
Project Euler - Problem 3

Name: Largest prime factor

Description:
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""

# Note: This code should work, but it is SLOW.
# TODO: Optimize code.

from math import sqrt, floor


def is_prime(num):

    return all(num % n for n in range(2, floor(sqrt(num)) + 1))


def largest_prime_factor(num):

    factors = [n for n in range(2, floor(num/2) + 1) if (num/n).is_integer()]

    return max(n for n in factors if is_prime(n))


print(largest_prime_factor(600_851_475_143))