# fp = "test.txt"
# X, Y = 11, 7
fp = "input.txt"
X, Y = 101, 103

robos = []

with open(fp) as f:
    for line in f:
        line = line.strip()
        p, v = line.split()
        p = p.lstrip("p=")
        x, y = p.split(",")
        v = v.lstrip("v=")
        vx, vy = v.split(",")
        robos.append((int(x), int(y), int(vx), int(vy)))


def move(x, y, vx, vy):
    return (x + vx) % X, (y + vy) % Y


q1 = 0
q2 = 0
q3 = 0
q4 = 0

for robo in robos:
    x, y, vx, vy = robo
    for _ in range(100):
        x, y = move(x, y, vx, vy)
    if x < X // 2 and y < Y // 2:
        q1 += 1
    elif x < X // 2 and y > Y // 2:
        q2 += 1
    elif x > X // 2 and y < Y // 2:
        q3 += 1
    elif x > X // 2 and y > Y // 2:
        q4 += 1

print(q1 * q2 * q3 * q4)
