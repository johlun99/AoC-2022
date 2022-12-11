lines = [line.strip() for line in open("input.txt", "r")]

def parseInput(data):
    output = []
    for line in data:
        row = []
        elves = line.split(",")

        row.append([int(val) for val in elves[0].split("-")])
        row.append([int(val) for val in elves[1].split("-")])

        output.append(row)

    return output

data = parseInput(lines)

countFullyCovered = 0
countOverlap = 0

for row in data:
    if row[0][0] <= row[1][0] and row[0][1] >= row[1][1]:
        countFullyCovered += 1
    elif row[0][0] >= row[1][0] and row[0][1] <= row[1][1]:
        countFullyCovered += 1

    if row[0][0] <= row[1][1] and row[0][1] >= row[0][0]:
        countOverlap += 1


print("Part 1: " + str(countFullyCovered))
print("Part 2: " + str(countOverlap))
