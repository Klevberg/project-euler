'''
Project Euler - Problem 1

Name: Multiples of 3 and 5

Description:
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''

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