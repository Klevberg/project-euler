# Name:     Self powers
# Source:   https://projecteuler.net/problem=48


last_digits = lambda n, x: int(str(n)[-x:]) # returns the last x digits of n.


self_powers = lambda num: last_digits(sum(last_digits(n**n, 10) for n in range(1, num + 1)), 10)


print(self_powers(1000))
