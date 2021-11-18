# Name:     Lattice paths
# Source:   https://projecteuler.net/problem=15


memoize_dict = {} # (x, y) = (amount of paths from point to end)

    
find_paths = lambda width, height: [memoize_dict.setdefault((x, y), (memoize_dict.get((x + 1, y), 1) if x + 1 <= width else 0) + (memoize_dict.get((x, y + 1), 1) if y + 1 <= height else 0)) for y in range(height, -1, -1) for x in range(width, -1, -1) if (x, y) != (width, height)][-1]


print(find_paths(20, 20))
