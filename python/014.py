# Name:     Longest Collatz sequence
# Source:   https://projecteuler.net/problem=14


memoize_dict = {1: 1}


def get_seq_length(num):

    acc, length = num, 1

    while acc not in memoize_dict: acc = acc//2 if acc % 2 == 0 else 3*acc + 1; length += 1

    return memoize_dict.setdefault(num, length + memoize_dict[acc])

    
longest_collatz_seq = lambda num: max((get_seq_length(n), n) for n in range(1, num, 2 if num > 73 else 1))[1]


print(longest_collatz_seq(1_000_000))
