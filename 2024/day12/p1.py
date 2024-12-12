import sys

M = []
for line in sys.stdin:
    M.append(list(line.strip()))

X = len(M)
Y = len(M[0])

seen = set()


def dfs(x, y):
    if (x, y) in seen:
        return 0, 0
    seen.add((x, y))
    area = 1
    peri = 0
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        i, j = x + dx, y + dy
        if 0 <= i < X and 0 <= j < Y:
            if M[i][j] == M[x][y]:
                a, p = dfs(i, j)
                area += a
                peri += p
            else:
                peri += 1
        else:
            peri += 1
    return area, peri


ans = 0
for x in range(X):
    for y in range(Y):
        a, p = dfs(x, y)
        ans += a * p

print(ans)
