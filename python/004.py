# Name:     Largest palindrome product
# Source:   https://projecteuler.net/problem=4


def largest_palindrome_product(digits):

    rng = range(int("9"*digits), 10**(digits - 1), -1)

    return max(p for x in rng for y in rng if (num_s := str(p := x*y)).endswith(num_s[:len(num_s)//2][::-1]))


print(largest_palindrome_product(3))
