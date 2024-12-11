from functools import cache

M = []

import sys

for line in sys.stdin:
    M.append([int(n) for n in line.strip()])

X = len(M)
Y = len(M[0])


@cache
def score(i, j):
    if M[i][j] == 9:
        return 1
    ret = 0
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        x, y = i + dx, j + dy
        if 0 <= x < X and 0 <= y < Y and M[x][y] == M[i][j] + 1:
            ret += score(x, y)
    return ret


ans = 0
for i in range(X):
    for j in range(Y):
        if M[i][j] == 0:
            ans += score(i, j)

print(ans)
