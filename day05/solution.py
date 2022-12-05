stackLines = []
movements = []

def getMovement(line):
    parts = line.split(" ")
    return [int(parts[1].strip()), int(parts[3].strip()), int(parts[5].strip())]

with open("input.txt", "r") as f:
    for line in f.readlines():
        if (line[0] == 'm'):
            movements.append(getMovement(line))

stacks = [
    ['Q', 'W', 'P', 'S', 'Z', 'R', 'H', 'D'],
    ['V', 'B', 'R', 'W', 'Q', 'H', 'F'],
    ['C', 'V', 'S', 'H'],
    ['H', 'F', 'G'],
    ['P', 'G', 'J', 'B', 'Z'],
    ['Q', 'T', 'J', 'H', 'W', 'F', 'L'],
    ['Z', 'T', 'W', 'D', 'L', 'V', 'J', 'N'],
    ['D', 'T', 'Z', 'C', 'J', 'G', 'H', 'F'],
    ['W', 'P', 'V', 'M', 'B', 'H']
]

for move in movements:
    for i in range(move[0]):
        stacks[move[2] - 1].append(stacks[move[1] - 1].pop())

print(stacks)
msg = ""
for col in stacks:
    msg += str(col[-1])

print("part 1: " + msg)


stacks = [
    ['Q', 'W', 'P', 'S', 'Z', 'R', 'H', 'D'],
    ['V', 'B', 'R', 'W', 'Q', 'H', 'F'],
    ['C', 'V', 'S', 'H'],
    ['H', 'F', 'G'],
    ['P', 'G', 'J', 'B', 'Z'],
    ['Q', 'T', 'J', 'H', 'W', 'F', 'L'],
    ['Z', 'T', 'W', 'D', 'L', 'V', 'J', 'N'],
    ['D', 'T', 'Z', 'C', 'J', 'G', 'H', 'F'],
    ['W', 'P', 'V', 'M', 'B', 'H']
]

for move in movements:
    temp = []
    for i in range(move[0]):
        temp.append(stacks[move[1] - 1].pop())

    temp = temp[::-1]
    stacks[move[2] - 1] = stacks[move[2] - 1] + temp

msg = ""
for col in stacks:
    msg += str(col[-1])

print("part 2: " + msg)
