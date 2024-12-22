import sys

pad1 = [
    "789",
    "456",
    "123",
    ".0A",
]

pad2 = [
    ".^A",
    "<v>",
]


def get_pos(pad):
    ret = {}
    for x, line in enumerate(pad):
        for y, c in enumerate(line):
            ret[c] = (x, y)
    return ret


def all_pos_p2p(p1, p2, pad, pos):
    if p1 == "." or p2 == ".":
        return []
    if p1 == p2:
        return ["A"]
    x1, y1 = pos[p1]
    x2, y2 = pos[p2]
    ret = []
    if x1 < x2:
        ret += ["v" + s for s in all_pos_p2p(pad[x1 + 1][y1], p2, pad, pos)]
    elif x1 > x2:
        ret += ["^" + s for s in all_pos_p2p(pad[x1 - 1][y1], p2, pad, pos)]
    if y1 < y2:
        ret += [">" + s for s in all_pos_p2p(pad[x1][y1 + 1], p2, pad, pos)]
    elif y1 > y2:
        ret += ["<" + s for s in all_pos_p2p(pad[x1][y1 - 1], p2, pad, pos)]
    return ret


def all_pos(prev, line, pad, pos):
    if not line:
        return [""]
    s1 = all_pos_p2p(prev, line[0], pad, pos)
    s2 = all_pos(line[0], line[1:], pad, pos)
    return [x + y for x in s1 for y in s2]


def gen(line, pad):
    pos = get_pos(pad)
    x, y = pos["A"]
    ret = ""
    for c in line:
        if pad[x][y] == ".":
            raise Exception("Invalid")
        if c == "^":
            x -= 1
        elif c == "v":
            x += 1
        elif c == ">":
            y += 1
        elif c == "<":
            y -= 1
        elif c == "A":
            ret += pad[x][y]
    return ret


def validate(line, ans):
    print(ans)
    ans = gen(ans, pad2)
    print(ans)
    ans = gen(ans, pad2)
    print(ans)
    ans = gen(ans, pad1)
    print(ans)
    assert ans == line


def score(line):
    ps = all_pos("A", line, pad1, get_pos(pad1))
    ps = [s for p in ps for s in all_pos("A", p, pad2, get_pos(pad2))]
    ps = [s for p in ps for s in all_pos("A", p, pad2, get_pos(pad2))]
    ans = min([p for p in ps], key=len)
    validate(line, ans)
    return min(len(p) for p in ps)


ans = 0

for line in sys.stdin:
    line = line.strip()
    num = int(line[:-1])
    s = score(line)
    print(s, num)
    ans += num * s

print(ans)
