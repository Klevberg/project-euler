# Name:     Longest Collatz sequence
# Source:   https://projecteuler.net/problem=14

# TODO: Optimize code.


sequence_dict = {1: [1], 2: [2, 1]}


def collatz_sequence(num):

    if num == 1:
        return [1]
    
    sequence = []

    while num != 1:

        if num in sequence_dict:
            sequence.extend(sequence_dict.get(num))
            break

        sequence.append(num)

        num = num//2 if num % 2 == 0 else 3*num + 1
    
    return sequence


def longest_collatz_sequence(num):

    number, length = 0, 0
    
    for n in range(1, num, 2):
        sequence = collatz_sequence(n)

        sequence_dict[n] = sequence

        sequence_length = len(sequence)

        if sequence_length > length:
            number, length = n, sequence_length
    
    return number


print(longest_collatz_sequence(1_000_000))
