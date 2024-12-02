import sys

def is_safe(xs):
    diffs = []
    for x, y in zip(xs, xs[1:]):
        diffs.append(x - y)

    if not (all(d > 0 for d in diffs) or all(d < 0 for d in diffs)):
        return False
    
    return all(1<= abs(d) <= 3 for d in diffs)
        
def is_safe_with_rm(xs):
    if is_safe(xs):
        return True
    
    for i in range(len(xs)):
        if is_safe(xs[:i] + xs[i+1:]):
            return True
    
    return False

ans = 0
for line in sys.stdin:
    xs = [int(x) for x in line.split()]
    if is_safe_with_rm(xs):
        ans += 1

print(ans)

