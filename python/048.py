# Name:     Self powers
# Source:   https://projecteuler.net/problem=48


def self_powers(num):

    return int(str(sum(int(str(n**n)[-10:]) for n in range(1, num + 1)))[-10:])


print(self_powers(1000))
