# fp = "test.txt"
# X, Y = 11, 7
fp = "input.txt"
X, Y = 101, 103


robos = []

with open(fp) as f:
    for line in f:
        line = line.strip()
        p, v = line.split()
        p = p.lstrip("p=")
        x, y = p.split(",")
        v = v.lstrip("v=")
        vx, vy = v.split(",")
        robos.append((int(x), int(y), int(vx), int(vy)))


def move(x, y, vx, vy):
    return (x + vx) % X, (y + vy) % Y


def max_comp(robos):
    ps = {(x, y) for x, y, _, _ in robos}
    seen = set()

    def dfs(x, y):
        seen.add((x, y))
        ret = 1
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            i, j = x + dx, x + dy
            if 0 <= i < X and 0 <= j < Y and (i, j) in ps:
                if (i, j) not in seen:
                    ret += dfs(i, j)
        return ret

    ret = 0
    for x, y in ps:
        if (x, y) not in seen:
            ret = max(ret, dfs(x, y))
    return ret


def display(robos):
    ps = {(x, y) for x, y, _, _ in robos}
    for x in range(X):
        for y in range(Y):
            if (x, y) in ps:
                print("#", end="")
            else:
                print(".", end="")
        print()


for sec in range(1, 10000):
    if sec % 1000 == 0:
        print(sec)
    i = 0
    while i < len(robos):
        x, y, vx, vy = robos[i]
        x, y = move(x, y, vx, vy)
        robos[i] = (x, y, vx, vy)
        i += 1
    if max_comp(robos) > 10:
        print(sec)
        display(robos)
