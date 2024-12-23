import sys
from collections import defaultdict

G = defaultdict(set)

for line in sys.stdin:
    line = line.strip()
    x, y = line.split("-")
    G[x].add(y)
    G[y].add(x)


conn = defaultdict(set)
for x in G:
    for y in G[x]:
        for z in G[y]:
            if x != z and z in G[x] and all(z in G[n] for n in conn[x, y]):
                conn[x, y].add(z)


ans = max(conn.items(), key=lambda x: len(x[1]))
print(",".join(sorted(set(ans[0]) | ans[1])))
