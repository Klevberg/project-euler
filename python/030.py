# Name:     Digit fifth powers
# Source:   https://projecteuler.net/problem=30


def fifth_powers_sum():
    
    return sum(n for n in range(2, 200_000) if n == sum(map(lambda x: int(x)**5, str(n))))


print(fifth_powers_sum())
