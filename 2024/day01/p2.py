import sys
from collections import Counter

c1 = []
c2 = Counter()
for line in sys.stdin:
    x, y = line.split()
    c1.append(int(x))
    c2[int(y)] += 1

ans = 0
for x in c1:
    ans += x * c2[x]

print(ans)
