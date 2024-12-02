import sys

def is_safe(xs):
    diffs = []
    for x, y in zip(xs, xs[1:]):
        diffs.append(x - y)

    if not (all(d > 0 for d in diffs) or all(d < 0 for d in diffs)):
        return False
    
    return all(1<= abs(d) <= 3 for d in diffs)
        


ans = 0
for line in sys.stdin:
    xs = [int(x) for x in line.split()]
    if is_safe(xs):
        ans += 1

print(ans)

