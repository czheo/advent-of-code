import sys

c1 = []
c2 = []
for line in sys.stdin:
    x, y = line.split()
    c1.append(int(x))
    c2.append(int(y))

c1.sort()
c2.sort()

ans = 0
for x, y in zip(c1, c2):
    ans += abs(x - y)

print(ans)
