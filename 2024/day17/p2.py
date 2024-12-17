# Manually translated input program into
# while A != 0:
#     B = A % 8  # 24
#     B = B ^ 1  # 11
#     C = A // (2**B)  # 75
#     A = A // (2**3)  # 03
#     B = B ^ 4  # 14
#     B = B ^ C  # 40
#     print(B % 8)  # 55

# Manually simplifed into
# A = 32916674
# B = C = 0
# while A != 0:
#     B = (A % 8) ^ 5 ^ (A // (2 ** ((A % 8) ^ 1)))
#     A = A // 8
#     print(B % 8)

prog = [2, 4, 1, 1, 7, 5, 0, 3, 1, 4, 4, 0, 5, 5, 3, 0]


def find(i, A):
    if i < 0:
        return A
    for A in range(A * 8, (A + 1) * 8):
        B = (A % 8) ^ 5 ^ (A // (2 ** ((A % 8) ^ 1)))
        if prog[i] == B % 8:
            a = find(i - 1, A)
            if a >= 0:
                return a
    return -1


print(find(len(prog) - 1, 0))
