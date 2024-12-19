import sys
from functools import cache

towels = set()
onsens = []
p1 = True
for line in sys.stdin:
    line = line.strip()
    if not line:
        p1 = False
        continue
    if p1:
        towels = set(line.split(", "))
    else:
        onsens.append(line)

minl, maxl = min(len(t) for t in towels), max(len(t) for t in towels)


@cache
def ok(onsen):
    if not onsen:
        return 1

    ret = 0
    for i in range(minl, maxl + 1):
        if i > len(onsen):
            break
        if onsen[:i] in towels:
            ret += ok(onsen[i:])

    return ret


ans = 0
for onsen in onsens:
    ans += ok(onsen)

print(ans)
