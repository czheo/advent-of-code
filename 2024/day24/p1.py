import sys


def getValue(x, y, op, z):
    def val():
        if not isinstance(wires[x], int):
            wires[x] = wires[x]()
        if not isinstance(wires[y], int):
            wires[y] = wires[y]()
        if op == "AND":
            ret = wires[x] & wires[y]
        elif op == "OR":
            ret = wires[x] | wires[y]
        elif op == "XOR":
            ret = wires[x] ^ wires[y]
        else:
            raise Exception(f"Unknown op: {op}")
        wires[z] = ret
        return ret

    return val


p1 = True

wires = {}
for line in sys.stdin:
    line = line.strip()

    if not line:
        p1 = False
        continue

    if p1:
        x, n = line.split(": ")
        wires[x] = int(n)
    else:
        x_op_y, z = line.split(" -> ")
        x, op, y = x_op_y.split(" ")
        wires[z] = getValue(x, y, op, z)

res = {}
for k, v in wires.items():
    if k[0] == "z":
        if isinstance(v, int):
            res[k] = v
        else:
            res[k] = v()

ans = 0
for k, v in sorted(res.items()):
    ans |= v << int(k[1:])

print(ans)
