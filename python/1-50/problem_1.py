# Name:     Multiples of 3 and 5
# Source:   https://projecteuler.net/problem=1

def sum_of_multiples(num_below, *nums_multiple):

    multiples = []

    for num in nums_multiple:
        acc = num # accumulator

        while acc < num_below:
            if acc not in multiples:
                multiples.append(acc)
            acc += num

    return sum(multiples)


print(sum_of_multiples(1000, 3, 5))