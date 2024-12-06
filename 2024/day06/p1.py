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

d = '^'
while True:
    if d == '^':
        if x - 1 < 0:
            break
        if M[x-1][y] == "#":
            d = '>'
        else:
            x -= 1
            M[x][y] = 'X'
    elif d == '>':
        if y + 1 >= Y:
            break
        if M[x][y + 1] == "#":
            d = 'v'
        else:
            y += 1
            M[x][y] = 'X'
    elif d == 'v':
        if x + 1 >= X:
            break
        if M[x+1][y] == "#":
            d = '<'
        else:
            x += 1
            M[x][y] = 'X'
    elif d == '<':
        if y - 1 < 0:
            break
        if M[x][y-1] == "#":
            d = '^'
        else:
            y -= 1
            M[x][y] = 'X'
print(sum(row.count('X') for row in M))
