import sys
from collections import defaultdict   
from itertools import combinations

M = []

for line in sys.stdin:
    M.append(list(line.strip()))

X = len(M)
Y = len(M[0])

ants = defaultdict(set)

nodes = set()
for x in range(X):
    for y in range(Y):
        if M[x][y] != '.':
            ants[M[x][y]].add((x, y))
            nodes.add((x, y))


def compute_nodes(ps):
    for (x1, y1), (x2, y2) in combinations(ps, 2):
        i = 1
        while True:
            x = x1 + (x1 - x2) * i
            y = y1 + (y1 - y2) * i
            if 0 <= x < X and 0 <= y < Y:
                nodes.add((x, y))
            else:
                break
            i += 1

        i = 1
        while True:
            x = x2 + (x2 - x1) * i
            y = y2 + (y2 - y1) * i
            if 0 <= x < X and 0 <= y < Y:
                nodes.add((x, y))
            else:
                break
            i += 1


for ps in ants.values():
    compute_nodes(ps)

print(len(nodes))
