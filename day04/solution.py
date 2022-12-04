with open("input.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]


def getRange(section):
    output = [int(section.split("-")[0]), int(section.split("-")[1])]
    return output


counter = 0
for line in lines:
    if line == "":
        break
    firstSection = line.split(",")[0]
    secondSection = line.split(",")[1]
    firstRange = getRange(firstSection)
    secondRange = getRange(secondSection)

    if firstRange[0] <= secondRange[0] and firstRange[1] >= secondRange[1]:
        counter += 1

    elif secondRange[0] <= firstRange[0] and secondRange[1] >= firstRange[1]:
        counter += 1

print("Part 1: " + str(counter))

counter = 0
for line in lines:
    if line == "":
        break
    firstSection = line.split(",")[0]
    secondSection = line.split(",")[1]
    firstRange = getRange(firstSection)
    secondRange = getRange(secondSection)

    if firstRange[1] >= secondRange[0] and firstRange[0] <= secondRange[1]:
        counter += 1

    elif secondRange[1] >= firstRange[0] and secondRange[0] <= firstRange[1]:
        counter += 1

print("Part 2: " + str(counter))
