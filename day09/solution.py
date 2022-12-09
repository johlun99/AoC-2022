with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

headPos = {"x": 0, "y": 0}
tailPos = {"x": 0, "y": 0}

headPositions = []
visitedPositions = []


def addPosition():
    exists = False
    for pos in visitedPositions:
        if pos["x"] == tailPos["x"] and pos["y"] == tailPos["y"]:
            exists = True

    if exists == False:
        visitedPositions.append({"x": tailPos["x"], "y": tailPos["y"]})


def moveTailIfNecessary():
    moved = False

    if headPos["x"] - 1 > tailPos["x"]:
        moved = True
        tailPos["x"] = headPositions[-1]["x"]
        tailPos["y"] = headPositions[-1]["y"]
    elif headPos["x"] + 1 < tailPos["x"]:
        moved = True
        tailPos["x"] = headPositions[-1]["x"]
        tailPos["y"] = headPositions[-1]["y"]

    if headPos["y"] - 1 > tailPos["y"]:
        moved = True
        tailPos["x"] = headPositions[-1]["x"]
        tailPos["y"] = headPositions[-1]["y"]
    elif headPos["y"] + 1 < tailPos["y"]:
        moved = True
        tailPos["x"] = headPositions[-1]["x"]
        tailPos["y"] = headPositions[-1]["y"]

    addPosition()
    if moved:
        moveTailIfNecessary()


def moveHead(dir, steps):
    for i in range(steps):
        if dir == "R":
            headPos["x"] += 1
            moveTailIfNecessary()
        elif dir == "L":
            headPos["x"] -= 1
            moveTailIfNecessary()
        elif dir == "U":
            headPos["y"] += 1
            moveTailIfNecessary()
        elif dir == "D":
            headPos["y"] -= 1
            moveTailIfNecessary()

        headPositions.append({"x": headPos["x"], "y": headPos["y"]})


for move in lines:
    parts = move.split(" ")
    moveHead(parts[0], int(parts[1]))

print("part 1: " + str(len(visitedPositions)))

tailPos = []

for i in range(10):
    tailPos.append({"x": 0, "y": 0})

headPositions = []
visitedPositions = []


def printBoard():
    board = []
    for y in range(-10, 10):
        row = ""
        for x in range(-10, 10):
            if x == 0 and y == 0:
                row += "S"
                continue

            if tailPos[0]["x"] == x and tailPos[0]["y"] == y:
                row += "H"
                continue

            isTail = False
            for pos in tailPos:
                if pos["x"] == x and pos["y"] == y:
                    isTail = True

            if isTail:
                row += "T"

            else:
                row += "."
        board.append(row)

    for row in board:
        print(row)
    print("\n")


def moveHead2(dir):
    if dir == "R":
        tailPos[0]["x"] += 1
    elif dir == "L":
        tailPos[0]["x"] -= 1
    elif dir == "U":
        tailPos[0]["y"] -= 1
    elif dir == "D":
        tailPos[0]["y"] += 1


def moveTail2():
    for i in range(1, len(tailPos)):
        if tailPos[i]["y"] == tailPos[i - 1]["y"]:
            if tailPos[i]["x"] < tailPos[i - 1]["x"] - 1:
                tailPos[i]["x"] += 1
            elif tailPos[i]["x"] > tailPos[i - 1]["x"] + 1:
                tailPos[i]["x"] -= 1
        elif tailPos[i]["x"] == tailPos[i - 1]["x"]:
            if tailPos[i]["y"] < tailPos[i - 1]["y"] - 1:
                tailPos[i]["y"] += 1
            elif tailPos[i]["y"] > tailPos[i - 1]["y"] + 1:
                tailPos[i]["y"] -= 1
        elif tailPos[i]["x"] != tailPos[i - 1]["x"] and tailPos[i]["y"] != tailPos[i - 1]["y"]:
            if tailPos[i]["y"] < tailPos[i - 1]["y"] - 1:
                tailPos[i]["y"] += 1

                if tailPos[i]["x"] < tailPos[i - 1]["x"]:
                    tailPos[i]["x"] += 1
                else:
                    tailPos[i]["x"] -= 1
            elif tailPos[i]["y"] > tailPos[i - 1]["y"] + 1:
                tailPos[i]["y"] -= 1

                if tailPos[i]["x"] < tailPos[i - 1]["x"]:
                    tailPos[i]["x"] += 1
                else:
                    tailPos[i]["x"] -= 1

            elif tailPos[i]["x"] < tailPos[i - 1]["x"] - 1:
                tailPos[i]["x"] += 1

                if tailPos[i]["y"] < tailPos[i - 1]["y"]:
                    tailPos[i]["y"] += 1
                else:
                    tailPos[i]["y"] -= 1
            elif tailPos[i]["x"] > tailPos[i - 1]["x"] + 1:
                tailPos[i]["x"] -= 1

                if tailPos[i]["y"] < tailPos[i - 1]["y"]:
                    tailPos[i]["y"] += 1
                else:
                    tailPos[i]["y"] -= 1


def checkVisited():
    exists = False
    for pos in visitedPositions:
        if pos["x"] == tailPos[-1]["x"] and pos["y"] == tailPos[-1]["y"]:
            exists = True

    if exists == False:
        visitedPositions.append({"x": tailPos[-1]["x"], "y": tailPos[-1]["y"]})



visitedPositions = []
for move in lines:
    parts = move.split(" ")
    for i in range(int(parts[1])):
        moveHead2(parts[0])
        moveTail2()
        checkVisited()
        # printBoard()

print("Part 2: " + str(len(visitedPositions)))