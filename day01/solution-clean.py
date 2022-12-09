with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

def parseInput(values):
    data = [0]

    for value in values:
        if value.isdigit():
            data[-1] += int(value)
        else:
            data.append(0)

    return data


elvesCalories = parseInput(lines)
elvesCalories.sort(reverse=True)

print("Part 1: " + str(max(elvesCalories)))
print("Part 2: " + str(sum([elvesCalories[0], elvesCalories[1], elvesCalories[2]])))
