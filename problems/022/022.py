# Name:     Names scores
# Source:   https://projecteuler.net/problem=22


def name_scores(filename):

    with open(filename) as f:

        names = sorted(f.read().strip('"').split('","'))
        
        values = [sum(map(lambda x: ord(x) - 64, name)) for name in names]
        
        return sum((i + 1)*value for i, value in enumerate(values))


print(name_scores("names.txt"))
