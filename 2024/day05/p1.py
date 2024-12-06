import sys
from collections import defaultdict
from functools import cache

part1 = True
G = defaultdict(set)

def ordered(xs):
    @cache
    def le(x, y, xs):
        if y not in xs:
            return True
        if x in G[y]:
            return False
        for y_ in G[y]:
            if not le(x, y_, xs):
                return False
        return True
    for x, y in zip(xs, xs[1:]):
        if not le(x, y, tuple(xs)):
            return False
    return True

ans = 0
for line in sys.stdin:
    line = line.strip()
    if part1:
        if not line:
            part1 = False
            continue
        x, y = line.split("|")
        G[int(x)].add(int(y))
    else:
        xs = [int(x) for x in line.split(",")]
        if ordered(xs):
            ans += xs[len(xs) // 2]

print(ans)
