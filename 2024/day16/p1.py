import sys
from collections import (
    defaultdict,
)

M = []
for line in sys.stdin:
    M.append(list(line.strip()))

X = len(M)
Y = len(M[0])

sx = sy = 0
for x in range(X):
    for y in range(Y):
        if M[x][y] == "S":
            sx = x
            sy = y


def bfs(x, y):
    dist = defaultdict(lambda: float("inf"))
    dist[x, y, 0, 1] = 0
    dist[x, y, 1, 0] = 1000
    Q = [(x, y, 0, 1), (x, y, 1, 0)]
    while Q:
        Q.sort(key=lambda x: -dist[x])
        x, y, dx, dy = Q.pop()
        if M[x][y] == "E":
            return dist[x, y, dx, dy]
        for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = x + di, y + dj
            if (di, dj) == (-dx, -dy):
                # don't go back
                continue
            if M[nx][ny] == "#":
                continue
            d_dist = 1001
            if (di, dj) == (dx, dy):
                d_dist = 1
            if dist[nx, ny, di, dj] > dist[x, y, dx, dy] + d_dist:
                dist[nx, ny, di, dj] = dist[x, y, dx, dy] + d_dist
                Q.append((nx, ny, di, dj))


print(bfs(sx, sy))
