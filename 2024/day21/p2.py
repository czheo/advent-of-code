import sys
from math import inf
from itertools import permutations
from functools import cache

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


pos1 = get_pos(pad1)
pos2 = get_pos(pad2)


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


def is_valid(n, seq):
    x, y = pos2[n]
    for s in seq:
        if s == "v":
            x += 1
        elif s == "^":
            x -= 1
        elif s == ">":
            y += 1
        elif s == "<":
            y -= 1
        if pad2[x][y] == ".":
            return False
    return True


@cache
def robo(x, y, level):
    if level == 25:
        return 1
    x1, y1 = pos2[x]
    x2, y2 = pos2[y]
    if x1 < x2:
        dx = "v"
    elif x1 > x2:
        dx = "^"
    else:
        dx = ""
    if y1 < y2:
        dy = ">"
    elif y1 > y2:
        dy = "<"
    else:
        dy = ""
    seq = dx * abs(x1 - x2) + dy * abs(y1 - y2)
    ret = inf
    for ss in set(permutations(seq)):
        if not is_valid(x, ss):
            continue
        r = 0
        prev = "A"
        for s in ss:
            r += robo(prev, s, level + 1)
            prev = s
        r += robo(prev, "A", level + 1)
        ret = min(ret, r)
    return ret


def score2(c, line):
    if not line:
        return 0
    return robo(c, line[0], 0) + score2(line[0], line[1:])


def score(line):
    ps = all_pos("A", line, pad1, get_pos(pad1))
    return min(score2("A", p) for p in ps)


ans = 0

for line in sys.stdin:
    line = line.strip()
    num = int(line[:-1])
    s = score(line)
    print(s, num)
    ans += num * s

print(ans)
