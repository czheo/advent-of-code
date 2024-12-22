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


N = 2000


def compute(n):
    for _ in range(2000):
        n = secret(n)
    return n


import sys

ans = 0
for line in sys.stdin:
    n = int(line)
    ans += compute(n)
print(ans)
