import sys

M = []

for line in sys.stdin:
    M.append(line)

X, Y = len(M), len(M[0])

def check(x, y, dx, dy):
    match = "XMAS"
    i = 0
    while i < len(match) and 0 <= x < X and 0 <= y < Y and M[x][y] == match[i]:
        x += dx
        y += dy
        i += 1
    return i == len(match)

ans = 0
for x in range(X):
    for y in range(Y):
        ans += check(x, y, 0, 1)
        ans += check(x, y, 0, -1)
        ans += check(x, y, 1, 0)
        ans += check(x, y, -1, 0)
        ans += check(x, y, 1, 1)
        ans += check(x, y, -1, 1)
        ans += check(x, y, 1, -1)
        ans += check(x, y, -1, -1)

print(ans)
