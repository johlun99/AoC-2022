from functools import cmp_to_key

with open("input.txt", "r") as f:
    packetGroups = f.read().strip()

packets = []

def checkPair(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return -1
        elif left == right:
            return 0
        else:
            return 1
    elif isinstance(left, list) and isinstance(right, list):
        i = 0
        while i < len(left) and i < len(right):
            c = checkPair(left[i], right[i])
            if c == -1:
                return -1
            if c == 1:
                return 1
            i += 1
        if i == len(left) and i < len(right):
            return -1
        elif i == len(right) and i < len(left):
            return 1
        else:
            return 0
    elif isinstance(left, int) and isinstance(right, list):
        return checkPair([left], right)
    else:
        return checkPair(left, [right])


part1 = 0
for i, g in enumerate(packetGroups.split("\n\n")):
    left, right = g.split("\n")

    left = eval(left)
    right = eval(right)

    packets.append(left)
    packets.append(right)

    if checkPair(left, right) == -1:
        part1 += 1 + i

print("Part 1: " + str(part1))

packets.append([[2]])
packets.append([[6]])

packets = sorted(packets, key=cmp_to_key(lambda left, right: checkPair(left, right)))
part2 = 1
for i, p in enumerate(packets):
    if p == [[2]] or p == [[6]]:
        part2 *= i + 1

print("Part 2: " + str(part2))