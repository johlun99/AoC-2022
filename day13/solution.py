import json

with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

packets = []

for i in range(len(lines)):
    if lines[i] == "":
        packets.append([
            json.loads(lines[i - 2]),
            json.loads(lines[i - 1])
        ])


def checkPair(left, right):
    valid = True

    for i in range(len(left)):
        if isinstance(left[i], int) and isinstance(right[i], int):
            if left[i] == right[i] or left[i] < right[i]:
                continue
        
        if isinstance(left[i], list) and isinstance(right[i], int) or isinstance(right[i], list) and isinstance(left[i], int):
            if isinstance(left[i], list) and not checkPair(left[i], [right[i]]):
                valid = False
                break
            elif isinstance(right[i], list) and not checkPair(right[i], [left[i]]):
                valid = False
                break

    return valid


for p in packets:
    left = p[0]
    right = p[1]

    print(type(left))
    print(isinstance(left, list))

    valid = checkPair(left, right)
    print("valid: " + str(valid))