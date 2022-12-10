from typing import List

with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

signalStrengths = []
execStack = []
i = 0
x = 1
cycle = 0
while i < len(lines) + 1:
    cycle += 1

    if (cycle == 20 or
        cycle == 60 or
        cycle == 100 or
        cycle == 140 or
        cycle == 180 or
        cycle == 220):
        signalStrengths.append(x * cycle)

    if len(execStack) > 0:
        for j in range(len(execStack)):
            execStack[j][0] -= 1
            if execStack[j][0] == 0:
                x += execStack[j][1]
                del execStack[j]
        continue

    if i >= len(lines) or lines[i] == "noop":
        i += 1
        continue

    parts = lines[i].split(" ")
    if parts[0] == "addx":
        execStack.append([1, int(parts[1])])
        i += 1

#print(execStack)
#print(signalStrengths)
print("Part 1: " + str(sum(signalStrengths)))

execStack = []
i = 0
x = 1
crt = []
pixelPos = 0
currentPos = 0
while i < len(lines) + 1:
    printString = ""
    pixelPos = x
    currentPos += 1

    if (currentPos == x or
        currentPos == x + 1 or
        currentPos == x + 2):
        crt.append("#")
    else:
        crt.append(".")

    if currentPos > 39:
        currentPos = 0

    if len(execStack) > 0:
        for j in range(len(execStack)):
            execStack[j][0] -= 1
            if execStack[j][0] == 0:
                x += execStack[j][1]
                del execStack[j]
        continue

    if i >= len(lines) or lines[i] == "noop":
        i += 1
        continue

    parts = lines[i].split(" ")
    if parts[0] == "addx":
        execStack.append([1, int(parts[1])])
        i += 1

print("\nPart 2:")
printString = ""
for p in crt:
    printString += p
    if len(printString) > 39:
        print(printString)
        printString = ""