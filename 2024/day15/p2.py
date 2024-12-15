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
        l = []
        for c in line:
            if c == "#":
                l += list("##")
            elif c == "O":
                l += list("[]")
            elif c == ".":
                l += list("..")
            elif c == "@":
                l += list("@.")
            else:
                raise Exception("Unknown char: " + c)
        M.append(l)
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
    def move_obj(x, y, dx, dy, check=True):
        if M[x][y] == "#":
            return False
        elif M[x][y] == ".":
            return True
        else:
            if check:
                return move_box(x, y, dx, dy, check)
            else:
                if move_box(x, y, dx, dy, check=True):
                    return move_box(x, y, dx, dy, check=False)
                else:
                    return False

    def move_box(x, y, dx, dy, check=False):
        if dy == 0:
            if M[x][y] == "[":
                if move_obj(x + dx, y, dx, dy, check) and move_obj(
                    x + dx, y + 1, dx, dy, check
                ):
                    if not check:
                        M[x][y] = "."
                        M[x][y + 1] = "."
                        M[x + dx][y] = "["
                        M[x + dx][y + 1] = "]"
                    return True
            elif M[x][y] == "]":
                if move_obj(x + dx, y, dx, dy, check) and move_obj(
                    x + dx, y - 1, dx, dy, check
                ):
                    if not check:
                        M[x + dx][y] = "]"
                        M[x + dx][y - 1] = "["
                        M[x][y] = "."
                        M[x][y - 1] = "."
                    return True
        else:
            assert dx == 0
            if M[x][y] == "[":
                assert dy == 1
                if move_obj(x, y + 2, dx, dy, check):
                    if not check:
                        M[x][y] = "."
                        M[x][y + 1] = "["
                        M[x][y + 2] = "]"
                    return True
            else:
                assert dy == -1
                if move_obj(x, y - 2, dx, dy, check):
                    if not check:
                        M[x][y] = "."
                        M[x][y - 1] = "]"
                        M[x][y - 2] = "["
                    return True
        return False

    global rx, ry
    if move_obj(rx + dx, ry + dy, dx, dy, check=False):
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
        if M[i][j] == "[":
            ans += i * 100 + j
print(ans)
