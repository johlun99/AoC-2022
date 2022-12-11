import operator

lines = [line.strip() for line in open("input.txt", "r")]

monkeys = {}
currentMonkey = {}
currentId = 0

for line in lines:
    if len(line) == 0:
        monkeys[currentId] = currentMonkey
        currentMonkey = {}

    elif line.startswith("Monkey"):
        currentId = int(line.split(" ")[1].replace(":", ""))

    elif line.startswith("Starting"):
        parts = line.split(": ")
        currentMonkey["items"] = [int(item) for item in parts[1].split(", ")]

    elif line.startswith("Operation"):
        currentMonkey["operation"] = line.split(": ")[1].replace("new = ", "")

    elif line.startswith("Test"):
        currentMonkey["test"] = int(line.split(": ")[1].split(" ")[-1])

    elif line.startswith("If true"):
        currentMonkey["true"] = line.split(" ")[-1]

    elif line.startswith("If false"):
        currentMonkey["false"] = line.split(" ")[-1]

monkeys[currentId] = currentMonkey
monkeyInspectCount = {}

for monkey in monkeys:
    monkeyInspectCount[monkey] = 0

def iterateMonkeys():
    toBeMoved = {}
    for monkey in monkeys:
        index = monkey

        for item in monkeys[index]["items"]:
            monkeyInspectCount[monkey] += 1
            worryLevel = int(eval(monkeys[index]["operation"].replace("old", str(item))) / 3)

            if worryLevel % monkeys[index]["test"] == 0:
                targetMonkey = int(monkeys[index]["true"])

            else:
                targetMonkey = int(monkeys[index]["false"])

            """ print(worryLevel)
            monkeys[targetMonkey]["items"].append(worryLevel)
            monkeys[index]["items"].remove(item)
            """
            if targetMonkey in toBeMoved:
                toBeMoved[targetMonkey].append({"item": item, "worry": worryLevel})
            else:
                toBeMoved[targetMonkey] = [{"item": item, "worry": worryLevel}]

        for target in toBeMoved:
            for item in toBeMoved[target]:
                monkeys[target]["items"].append(item["worry"])
                monkeys[index]["items"].remove(item["item"])

        toBeMoved = {}


for i in range(20):
    iterateMonkeys()

for index in monkeys:
    print("ID: " + str(index))
    print("Items")
    print(monkeys[index]["items"])

monkeyInspectCountSorted = sorted(monkeyInspectCount.items(), key=lambda x:x[1], reverse=True)
answer = monkeyInspectCountSorted[0][1] * monkeyInspectCountSorted[1][1]

print("Part1: " + str(answer))