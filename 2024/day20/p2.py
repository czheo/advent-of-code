import sys
from collections import deque, Counter

M = []

for line in sys.stdin:
    line = line.strip()
    M.append(list(line))

X = len(M)
Y = len(M[0])

sx = sy = 0
ex = ey = 0

for i in range(X):
    for j in range(Y):
        if M[i][j] == "S":
            sx = i
            sy = j
        elif M[i][j] == "E":
            ex = i
            ey = j


def bfs():
    Q = deque([(sx, sy)])
    ret = 0
    seen = set(Q)
    while Q:
        for _ in range(len(Q)):
            x, y = Q.popleft()
            if x == ex and y == ey:
                return ret
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                if nx < 0 or nx >= X or ny < 0 or ny >= Y:
                    continue
                if (nx, ny) in seen:
                    continue
                if M[nx][ny] == "#":
                    continue
                seen.add((nx, ny))
                Q.append((nx, ny))
        ret += 1
    return -1


base = bfs()
print(base)


def bfs2(sx, sy):
    dists = {}
    Q = deque([(sx, sy)])
    ret = 0
    seen = set(Q)
    while Q:
        for _ in range(len(Q)):
            x, y = Q.popleft()
            dists[x, y] = ret
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                if nx < 0 or nx >= X or ny < 0 or ny >= Y:
                    continue
                if (nx, ny) in seen:
                    continue
                if M[nx][ny] == "#":
                    continue
                seen.add((nx, ny))
                Q.append((nx, ny))
        ret += 1
    return dists


sdists = bfs2(sx, sy)
edists = bfs2(ex, ey)
ans = 0
for (sx, sy), ds in sdists.items():
    for (ex, ey), de in edists.items():
        d = abs(sx - ex) + abs(sy - ey)
        if d <= 20:
            save = base - (d + ds + de)
            if save >= 100:
                ans += 1
print(ans)
