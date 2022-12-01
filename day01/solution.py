with open("input.txt", "r") as f:
    input = [line.strip() for line in f.readlines()]

elves = []
elf = []
elvesSum = []

for line in input:
    if line.isdigit():
        elf.append(int(line))
    else:
        elves.append(elf)
        elf = []

for line in elves:
    sum = 0
    for cal in line:
        sum += int(cal)
    elvesSum.append(sum)

elvesSum = sorted(elvesSum, reverse=True)

print("Part 1: " + str(elvesSum[0]))
print("Part 2: " + str(elvesSum[0] + elvesSum[1] + elvesSum[2]))