import sys

blocks = []

line = sys.stdin.read().strip()

free = False
files = []
for c in line:
    n = int(c)
    if free:
        for _ in range(n):
            blocks.append(-1)
    else:
        for _ in range(n):
            blocks.append(len(files))
        files.append((len(blocks) - n, len(blocks) - 1))
    free = not free

# print(blocks)
# print(files)


def find_free(size, until):
    global find_start
    found_free = False
    for i in range(find_start, until + 1):
        if blocks[i] == -1:
            found_free = True
        if not found_free:
            find_start = i
        if sum(blocks[i : i + size]) == -1 * size:
            return i
    return -1


def set_n(i, j, n):
    while i <= j:
        blocks[i] = n
        i += 1


find_start = 0
fp = len(files) - 1
while fp > 0:
    # print(fp)
    s, e = files[fp]
    size = e - s + 1
    idx = find_free(size, s - size)
    if idx != -1:
        set_n(s, e, -1)
        set_n(idx, idx + size - 1, fp)
    fp -= 1

# print(blocks)
print(sum(i * n for i, n in enumerate(blocks) if n >= 0))
