# Name:     Maximum path sum II
# Source:   https://projecteuler.net/problem=67


with open("triangle.txt") as f: data = f.read()
tree = [list(map(int, row.split())) for row in data.strip().split('\n')]

memoize_dict = {} # (row, index) : (sum of max path from tree[row][index])


find_max_sum = lambda row, index: memoize_dict.setdefault((row, index), tree[row][index] + max(memoize_dict[(row + 1, index)], memoize_dict[(row + 1, index + 1)]) if (row + 1) < len(tree) else tree[row][index])

print([find_max_sum(row, index) for row in range(len(tree) - 1, -1, -1) for index in range(len(tree[row]))][-1])
