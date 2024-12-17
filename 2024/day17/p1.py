import sys

A = B = C = 0
program = []
for line in sys.stdin:
    line = line.strip()
    if line.startswith("Register A"):
        A = int(line.split(":")[1])
    elif line.startswith("Register B"):
        B = int(line.split(":")[1])
    elif line.startswith("Register C"):
        C = int(line.split(":")[1])
    elif line.startswith("Program"):
        program = [int(x) for x in line.split(":")[1].split(",")]


i = 0
output = []
while i < len(program):
    inst, op = program[i], program[i + 1]

    def compo(op):
        if op == 4:
            return A
        elif op == 5:
            return B
        elif op == 6:
            return C
        elif op >= 7:
            raise ValueError
        return op

    if inst == 0:
        A = A // (2 ** compo(op))
    elif inst == 1:
        B = B ^ op
    elif inst == 2:
        B = compo(op) % 8
    elif inst == 3:
        if A != 0:
            i = op
            continue
    elif inst == 4:
        B = B ^ C
    elif inst == 5:
        output.append(compo(op) % 8)
    elif inst == 6:
        B = A // (2 ** compo(op))
    elif inst == 7:
        C = A // (2 ** compo(op))
    i += 2

print(A, B, C)
print(",".join(str(x) for x in output))
