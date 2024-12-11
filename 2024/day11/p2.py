from functools import cache

stones = [0, 4, 4979, 24, 4356119, 914, 85734, 698829]
# stones = [125, 17]


@cache
def compute(x, times):
    if times == 0:
        return 1
    if x == 0:
        return compute(1, times - 1)
    else:
        s = str(x)
        if len(s) % 2 == 0:
            return compute(int(s[: len(s) // 2]), times - 1) + compute(
                int(s[len(s) // 2 :]), times - 1
            )
        else:
            return compute(2024 * x, times - 1)


ans = 0
for x in stones:
    ans += compute(x, 75)

print(ans)
