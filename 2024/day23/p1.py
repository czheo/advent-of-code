import sys
from collections import defaultdict

G = defaultdict(set)

for line in sys.stdin:
    line = line.strip()
    x, y = line.split("-")
    G[x].add(y)
    G[y].add(x)


conn = set()
for x in G:
    for y in G[x]:
        for z in G[y]:
            if x != z and x in G[z] and (x[0] == "t" or y[0] == "t" or z[0] == "t"):
                conn.add(tuple(sorted([x, y, z])))

for c in sorted(conn):
    print(c)

print(len(conn))
