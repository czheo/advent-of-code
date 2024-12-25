import sys

locks = []
keys = []


def parse(schema):
    if schema[0] == "#####":
        out = locks
    else:
        out = keys
    ret = []
    for col in zip(*schema):
        ret.append(col.count("#") - 1)
    out.append(ret)


schema = []
for line in sys.stdin:
    line = line.strip()
    if not line:
        parse(schema)
        schema.clear()
        continue
    schema.append(line)

parse(schema)


def fits(lock, key):
    for x, y in zip(lock, key):
        if x + y > 5:
            return False
    return True


ans = 0
for lock in locks:
    for key in keys:
        if fits(lock, key):
            ans += 1
            print(lock, key)
print(ans)
