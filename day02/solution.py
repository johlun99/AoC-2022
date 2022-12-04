data = []
with open("input.txt", "r") as f:
    for line in f.readlines():
        line = line.strip()
        if (len(line) > 0):
            temp = []
            parts = line.split(" ")
            temp.append(parts[0])
            temp.append(parts[1])

            data.append(temp)


def part01(data):
    horizontal = 0
    depth = 0

    for vals in data:
        if (vals[0] == "forward"):
            horizontal += int(vals[1])

        elif vals[0] == "down":
            depth += int(vals[1])

        elif vals[0] == "up":
            depth -= int(vals[1])

    print("Part 1: " + str(depth * horizontal))

def part02(data):
    horizontal = 0
    depth = 0
    aim = 0

    for vals in data:
        if (vals[0] == "forward"):
            horizontal += int(vals[1])
            depth += (aim * int(vals[1]))

        elif (vals[0] == "down"):
            aim += int(vals[1])

        elif vals[0] == "up":
            aim -= int(vals[1])

    print("Part 2: " + str(horizontal * depth))

part01(data)
part02(data)