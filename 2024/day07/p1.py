import sys

def ok(x, ys):
    if x < 0:
        return False
    if len(ys) == 1:
        return x == ys[0]
    y = ys.pop()
    if ok(x - y, ys):
        return True
    z, r = divmod(x, y)
    if r == 0 and ok(z, ys):
        return True
    else:
        ys.append(y)
        return False

ans = 0
for line in sys.stdin:
    x, ys = line.split(":")
    x = int(x)
    ys = [int(y) for y in ys.strip().split()]
    if ok(x, ys):
        ans += x

print(ans)
