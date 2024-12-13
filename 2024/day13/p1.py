import sys
import re

Q = []
Qs = []
for line in sys.stdin:
    line = line.strip()
    if not line:
        Qs.append(Q)
        Q = []
    elif "Button A" in line:
        matched = re.match(r".*X\+(\d+), Y\+(\d+)", line)
        if matched:
            Q.append((int(matched.group(1)), int(matched.group(2))))
    elif "Button B" in line:
        matched = re.match(r".*X\+(\d+), Y\+(\d+)", line)
        if matched:
            Q.append((int(matched.group(1)), int(matched.group(2))))
    else:
        matched = re.match(r".*X=(\d+), Y=(\d+)", line)
        if matched:
            Q.append(
                (
                    int(matched.group(1)),
                    int(matched.group(2)),
                )
            )
Qs.append(Q)


from math import inf


def cost(q):
    (x1, y1), (x2, y2), (x, y) = q
    i = 0
    while True:
        if x - i * x1 >= 0 and y - i * y1 >= 0:
            nx, rx = divmod(x - i * x1, x2)
            ny, ry = divmod(y - i * y1, y2)
            if rx == 0 and ry == 0 and nx == ny:
                return 3 * i + nx
        else:
            return inf
        i += 1


ans = 0
for q in Qs:
    c = cost(q)
    if c != inf:
        ans += c

print(ans)
