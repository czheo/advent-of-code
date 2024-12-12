import sys

M = []
for line in sys.stdin:
    M.append(list(line.strip()))

X = len(M)
Y = len(M[0])

seen = set()


def dfs(x, y):
    if (x, y) in seen:
        return 0, set()
    seen.add((x, y))
    area = 1
    peri = set()
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        i, j = x + dx, y + dy
        if 0 <= i < X and 0 <= j < Y:
            if M[i][j] == M[x][y]:
                a, p = dfs(i, j)
                area += a
                peri |= p
            else:
                peri.add((x, y, dx, dy))
        else:
            peri.add((x, y, dx, dy))
    return area, peri


from collections import defaultdict


def count(edges):
    ret = 0
    d = defaultdict(list)
    for x, y in edges:
        d[x].append(y)
    for x, ys in d.items():
        ys.sort()
        prev = -100
        for y in ys:
            if y != prev + 1:
                ret += 1
            prev = y
    return ret


def sides(edges):
    ret = 0
    d = defaultdict(set)
    for x, y, dx, dy in edges:
        d[(dx, dy)].add((x, y))
    for (dx, dy), es in d.items():
        if dy == 0:
            ret += count(es)
        else:
            es = [(b, a) for a, b in es]
            ret += count(es)
    return ret


ans = 0
for x in range(X):
    for y in range(Y):
        a, p = dfs(x, y)
        ans += a * sides(p)

print(ans)
