import sys

p1 = True
M = []
steps = ""
for line in sys.stdin:
    line = line.strip()
    if not line:
        p1 = False
        continue
    if p1:
        M.append(list(line))
    else:
        steps += line

X = len(M)
Y = len(M[0])

rx, ry = 0, 0
for i in range(X):
    for j in range(Y):
        if M[i][j] == "@":
            rx, ry = i, j


def print_map():
    for i in range(X):
        for j in range(Y):
            print(M[i][j], end="")
        print()


def move(dx, dy):
    def move_obj(x, y, dx, dy):
        if M[x][y] == "#":
            return False
        elif M[x][y] == ".":
            return True
        elif M[x][y] == "O":
            if move_obj(x + dx, y + dy, dx, dy):
                M[x + dx][y + dy] = "O"
                M[x][y] = "."
                return True
            else:
                return False

    global rx, ry
    if move_obj(rx + dx, ry + dy, dx, dy):
        M[rx + dx][ry + dy] = "@"
        M[rx][ry] = "."
        rx = rx + dx
        ry = ry + dy


for s in steps:
    if s == "v":
        move(1, 0)
    elif s == "^":
        move(-1, 0)
    elif s == ">":
        move(0, 1)
    elif s == "<":
        move(0, -1)
    else:
        raise Exception("Unknown step: " + s)
    # print("Move:", s)
    # print_map()

ans = 0
for i in range(X):
    for j in range(Y):
        if M[i][j] == "O":
            ans += i * 100 + j
print(ans)
