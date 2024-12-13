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
                    10000000000000 + int(matched.group(1)),
                    10000000000000 + int(matched.group(2)),
                )
            )
Qs.append(Q)


from math import inf


def cost(q):
    """
    a1 * x + a2 * y = a
    b1 * x + b2 * y = b

    y = (a * b1 - b * a1) / (a2 * b1 - b2 * a1)
    x = (a - a2 * y) / a1
    """
    (a1, b1), (a2, b2), (a, b) = q
    y, r = divmod(a * b1 - b * a1, a2 * b1 - b2 * a1)
    if r == 0:
        x, r = divmod(a - a2 * y, a1)
        if r == 0:
            return x * 3 + y
    return inf


ans = 0
for q in Qs:
    c = cost(q)
    if c != inf:
        print(q)
        ans += c

print(ans)
