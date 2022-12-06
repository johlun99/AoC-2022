with open("input.txt", "r") as f:
    line = f.readline()

def removeBefore(items, border):
    for i in range(0, len(items)):
        if items[i] == border:
            return items[i+1:]

    return items

unique = []
for i in range(0, len(line)):
    if line[i] in unique:
        unique = removeBefore(unique, line[i])

    unique.append(line[i])
    if len(unique) == 4:
        print("part 1: " + str(i + 1))
        break


unique = []
for i in range(0, len(line)):
    if line[i] in unique:
        unique = removeBefore(unique, line[i])

    unique.append(line[i])
    if len(unique) == 14:
        print("part 2: " + str(i + 1))
        break
