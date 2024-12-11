import sys

blocks = []

line = sys.stdin.read().strip()

free = False
blocks = {}
frees = []
i = 0
fid = 0
for c in line:
    n = int(c)
    if n > 0:
        j = i + n - 1
        if free:
            frees.append((i, j))
        else:
            blocks[fid] = (i, j)
        i += n
    free = not free
    if free:
        fid += 1

print(blocks)
print(frees)

for fid in reversed(range(fid)):
    (bs, be) = blocks[fid]
    for i, (fs, fe) in enumerate(frees):
        if fe > bs:
            break
        if fe - fs >= be - bs:
            blocks[fid] = (fs, fs + be - bs)
            remain_free = fe - fs - (be - bs)
            if remain_free > 0:
                frees[i] = (fs + (be - bs) + 1, fe)
            else:
                frees.pop(i)
            break

ans = 0
for fid, (s, e) in blocks.items():
    ans += sum(fid * i for i in range(s, e + 1))

print(blocks)
print(frees)
print(ans)
