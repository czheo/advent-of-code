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
    def find_path(x, y, dx, dy):
        for i, j, di, dj in parents[(x, y, dx, dy)]:
            ret.add((i, j))
            find_path(i, j, di, dj)

    parents = defaultdict(set)
    dist = defaultdict(lambda: float("inf"))
    dist[x, y, 0, 1] = 0
    dist[x, y, 1, 0] = 1000
    Q = [(x, y, 0, 1), (x, y, 1, 0)]
    ret = set()
    min_dist = float("inf")
    while Q:
        Q.sort(key=lambda x: -dist[x])
        x, y, dx, dy = Q.pop()
        if M[x][y] == "E":
            if dist[x, y, dx, dy] > min_dist:
                return ret
            min_dist = dist[x, y, dx, dy]
            find_path(x, y, dx, dy)
            continue
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
            if dist[nx, ny, di, dj] >= dist[x, y, dx, dy] + d_dist:
                dist[nx, ny, di, dj] = dist[x, y, dx, dy] + d_dist
                Q.append((nx, ny, di, dj))
                parents[nx, ny, di, dj].add((x, y, dx, dy))
    return ret


print(len(bfs(sx, sy)) + 1)
