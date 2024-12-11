stones = [0, 4, 4979, 24, 4356119, 914, 85734, 698829]
# stones = [125, 17]
times = 25

for _ in range(times):
    i = 0
    while i < len(stones):
        if stones[i] == 0:
            stones[i] = 1
        else:
            s = str(stones[i])
            if len(s) % 2 == 0:
                stones[i] = int(s[: len(s) // 2])
                stones.insert(i + 1, int(s[len(s) // 2 :]))
                i += 1
            else:
                stones[i] *= 2024
        i += 1

print(len(stones))
