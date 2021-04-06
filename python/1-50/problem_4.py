"""
Project Euler - Problem 4

Name: Largest palindrome product

Description:
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""

from itertools import product


def is_palindrome(num):

    return str(num).endswith(str(num)[:len(str(num))//2][::-1])


def largest_palindrome_product(digits):

    max_ = int("9"*digits)
    min_ = int("1" + "0"*(digits - 1))
    range_ = range(max_, min_ - 1, -1)

    return max(x*y for x, y in product(range_, range_) if is_palindrome(x*y))


print(largest_palindrome_product(3))
