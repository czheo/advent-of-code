import sys

M = []

for line in sys.stdin:
    M.append(list(line.strip()))

x = 0
X = len(M)
Y = len(M[0])

while x < X:
    y = 0
    while y < Y:
        if M[x][y] == '^':
            M[x][y] = 'X'
            break
        y += 1
    if y < Y:
        break
    else:
        x += 1

def loop(x, y, i, j):
    M[i][j] = '#'
    d = '^'
    seen = set()
    ret = False
    while True:
        if (d, x, y) in seen:
            ret = True
            break
        if d == '^':
            if x - 1 < 0:
                break
            if M[x-1][y] == "#":
                d = '>'
            else:
                seen.add((d, x, y))
                x -= 1
        elif d == '>':
            if y + 1 >= Y:
                break
            if M[x][y + 1] == "#":
                d = 'v'
            else:
                seen.add((d, x, y))
                y += 1
        elif d == 'v':
            if x + 1 >= X:
                break
            if M[x+1][y] == "#":
                d = '<'
            else:
                seen.add((d, x, y))
                x += 1
        elif d == '<':
            if y - 1 < 0:
                break
            if M[x][y-1] == "#":
                d = '^'
            else:
                seen.add((d, x, y))
                y -= 1
    M[i][j] = '.'
    return ret

def main():
    ans = 0
    for i in range(X):
        for j in range(Y):
            if M[i][j] == '#' or (x == i and y == j):
                continue
            if loop(x, y, i, j):
                ans += 1
    print(ans)

main()
