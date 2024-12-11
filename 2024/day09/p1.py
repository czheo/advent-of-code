import sys

blocks = []

line = sys.stdin.read().strip()

free = False
i = 0
for c in line:
    n = int(c)
    for _ in range(n):
        if free:
            blocks.append(-1)
        else:
            blocks.append(i)
    free = not free
    if free:
        i += 1

print(blocks)

i = 0
j = len(blocks) - 1

while True:
    while blocks[i] != -1:
        i += 1
    while blocks[j] == -1:
        j -= 1
    if i >= j:
        break
    blocks[i], blocks[j] = blocks[j], blocks[i]

print(blocks)
print(sum(i * n for i, n in enumerate(blocks) if n >= 0))
