def secret(n):
    n = mix(n * 64, n)
    n = prune(n)
    n = mix(n // 32, n)
    n = prune(n)
    n = mix(n * 2048, n)
    n = prune(n)
    return n


def mix(n, secret):
    return n ^ secret


def prune(secret):
    return secret % 16777216


from collections import deque


def ones(n):
    return int(str(n)[-1])


from collections import Counter

cnts = Counter()


def seq(n):
    ret = [ones(n)]
    diffs = [()]
    win = deque()
    seen = set()
    for _ in range(2000):
        sec = secret(n)
        ret.append(ones(sec))
        n = sec
        win.append(ret[-1] - ret[-2])
        if len(win) > 4:
            win.popleft()
        diffs.append(tuple(win))
        if len(win) == 4:
            if tuple(win) in seen:
                continue
            else:
                cnts[tuple(win)] += ret[-1]
                seen.add(tuple(win))
    return ret[4:], diffs[4:]


import sys

for line in sys.stdin:
    n = int(line)
    seq(n)

print(cnts.most_common(1)[0])
