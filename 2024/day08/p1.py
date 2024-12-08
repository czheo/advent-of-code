import sys
from collections import defaultdict   
from itertools import combinations

M = []

for line in sys.stdin:
    M.append(list(line.strip()))

X = len(M)
Y = len(M[0])

ants = defaultdict(set)

for x in range(X):
    for y in range(Y):
        if M[x][y] != '.':
            ants[M[x][y]].add((x, y))

nodes = set()

def compute_nodes(ps):
    for (x1, y1), (x2, y2) in combinations(ps, 2):
        x = x1 + (x1 - x2)
        y = y1 + (y1 - y2)
        if 0 <= x < X and 0 <= y < Y:
            nodes.add((x, y))
        x = x2 + (x2 - x1)
        y = y2 + (y2 - y1)
        if 0 <= x < X and 0 <= y < Y:
            nodes.add((x, y))


for ps in ants.values():
    compute_nodes(ps)

print(len(nodes))

