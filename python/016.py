# Name:     Power digit sum
# Source:   https://projecteuler.net/problem=16


def power_digit_sum(exponent):

    return sum(list(map(int, str(2**exponent))))


print(power_digit_sum(1000))
