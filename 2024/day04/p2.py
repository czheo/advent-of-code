import sys

M = []

for line in sys.stdin:
    M.append(line)

X, Y = len(M), len(M[0])

def check(x, y, dx, dy):
    match = "MAS"
    i = 0
    while i < len(match) and 0 <= x < X and 0 <= y < Y and M[x][y] == match[i]:
        x += dx
        y += dy
        i += 1
    return i == len(match)

def checkx(x, y):
    return ((check(x-1,y-1,1,1) + check(x+1,y+1,-1,-1)) and 
            (check(x+1,y-1,-1,1) + check(x-1,y+1,1,-1)))


ans = 0
for x in range(X):
    for y in range(Y):
        ans += checkx(x, y)

print(ans)
