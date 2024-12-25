import sys

p1 = True
X = 0
Y = 0
WIRES = {}
for line in sys.stdin:
    line = line.strip()

    if not line:
        p1 = False
        continue

    if p1:
        x, n = line.split(": ")
        WIRES[x] = int(n)
        if x[0] == "x":
            X = int(n) << int(x[1:])
        elif x[0] == "y":
            Y = int(n) << int(x[1:])
    else:
        x_op_y, z = line.split(" -> ")
        x, op, y = x_op_y.split(" ")
        print(x, "->", f'{z} [label="{op}"]')
        print(y, "->", f'{z} [label="{op}"]')
        WIRES[z] = (x, op, y)

from functools import cache


@cache
def getVal(k):
    if isinstance(WIRES[k], int):
        return WIRES[k]
    else:
        x, op, y = WIRES[k]
        if op == "AND":
            ret = getVal(x) & getVal(y)
        elif op == "OR":
            ret = getVal(x) | getVal(y)
        elif op == "XOR":
            ret = getVal(x) ^ getVal(y)
        else:
            raise Exception(f"Unknown op {op}")
        return ret


res = {}
for k in WIRES.keys():
    if k[0] == "z":
        res[k] = getVal(k)

ans = 0
for k, v in sorted(res.items()):
    ans |= v << int(k[1:])

print(ans)
Z = X + Y
print("Z = ", Z)

x, y = "x00", "y00"
half_sum = "x00 XOR y00"
half_carry = "x00 AND y00"
sum = "half_sum XOR carry"
half_sc = "half_sum AND carry"
carry = "half_carry OR half_sc"


def find_wire(x, y, op, name):
    for k, v in WIRES.items():
        if v == (x, op, y) or v == (y, op, x):
            return k
    raise Exception(f"Can't find wire {x} {op} {y} for {name}")


def validate(i, carry=None):
    x, y = f"x{i:02d}", f"y{i:02d}"
    half_sum = find_wire(x, y, "XOR", f"half_sum{i:02d}")
    half_carry = find_wire(x, y, "AND", f"half_carry{i:02d}")
    if carry is None:
        sum = half_sum
        assert sum == f"z{i:02d}", f"{sum} != z{i:02d}"
        return half_carry
    else:
        sum = find_wire(half_sum, carry, "XOR", f"sum{i:02d}")
        assert sum == f"z{i:02d}", f"{sum} != z{i:02d}"
        half_sc = find_wire(half_sum, carry, "AND", f"half_sc{i:02d}")
        carry = find_wire(half_carry, half_sc, "OR", f"carry{i:02d}")
        return carry


carry = None
for i in range(0, 45):
    carry = validate(i, carry)
    print(carry)
