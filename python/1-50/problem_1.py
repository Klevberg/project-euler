def sum_of_multiples(num_below, *nums_multiple):

    if not nums_multiple:
        nums_multiple = (3, 5)

    multiples = []

    for num in nums_multiple:
        acc = num # accumulator

        while acc < num_below:
            multiples.append(acc)
            acc += num

    return sum(multiples)


print(sum_of_multiples(1000))