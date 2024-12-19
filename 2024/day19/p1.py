import sys

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


def ok(onsen):
    if onsen in towels:
        return True

    for i in range(minl, maxl + 1):
        if i > len(onsen):
            break
        if onsen[:i] in towels and ok(onsen[i:]):
            return True

    return False


ans = 0
for onsen in onsens:
    if ok(onsen):
        ans += 1

print(ans)
