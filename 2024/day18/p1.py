# X, Y = 6, 6
# filename = "test.txt"
# steps = 12

X, Y = 70, 70
filename = "input.txt"
steps = 1024

M = [["." for _ in range(Y + 1)] for _ in range(X + 1)]
n = 0
with open(filename) as f:
    for line in f:
        y, x = line.split(",")
        M[int(x)][int(y)] = "#"
        n += 1
        if n >= steps:
            break

for l in M:
    print("".join(l))

from collections import deque


def bfs():
    Q = deque()
    Q.append((0, 0))
    ret = 0
    seen = {(0, 0)}
    while Q:
        for _ in range(len(Q)):
            x, y = Q.popleft()
            if x == X and y == Y:
                return ret
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                i, j = x + dx, y + dy
                if i < 0 or i > X or j < 0 or j > Y:
                    continue
                if (i, j) in seen:
                    continue
                if M[i][j] == ".":
                    seen.add((i, j))
                    Q.append((i, j))
        ret += 1
    return ret


print(bfs())
