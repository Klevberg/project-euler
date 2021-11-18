# Name:     Power digit sum
# Source:   https://projecteuler.net/problem=16


power_digit_sum = lambda exp: sum(map(int, str(2**exp)))


print(power_digit_sum(1000))
