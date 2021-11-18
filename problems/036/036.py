# Name:     Double-base palindromes
# Source:   https://projecteuler.net/problem=36


def double_base_palindromes(below_num):

    is_palindrome = lambda s: s.endswith(s[:len(s)//2][::-1])

    return sum(n for n in range(below_num) if is_palindrome(str(n)) and is_palindrome(str(bin(n))[2:]))


print(double_base_palindromes(1_000_000))