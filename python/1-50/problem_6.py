# Name:     Sum square difference
# Source:   https://projecteuler.net/problem=6

def sum_of_square(num):
    
    return sum(n**2 for n in range(1, num + 1))


def square_of_sum(num):
    
    return sum(range(1, num + 1))**2


def difference(num):

    return square_of_sum(num) - sum_of_square(num)


print(difference(100))