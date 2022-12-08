with open("input.txt", "r") as f:
    trees = []
    for line in f.readlines():
        row = []
        for digit in line:
            if digit.isdigit():
                row.append(int(digit))
        trees.append(row)

def countEdges(trees):
    count = 0
    for y in range(len(trees)):
        for x in range(len(trees[y])):
            if y == 0 or x == 0:
                count += 1
            elif x == len(trees[y]) - 1:
                count += 1
            elif y == len(trees) - 1:
                count += 1
    return count

def checkVisibleTree(trees, x, y):
    visible = True
    for i in range(x - 1, -1, -1):
        if trees[y][i] >= trees[y][x]:
            visible = False

    if visible:
        return True
    visible = True

    for i in range(x + 1, len(trees[y])):
        if trees[y][i] >= trees[y][x]:
            visible = False

    if visible:
        return True
    visible = True

    for i in range(y - 1, -1, -1):
        if trees[i][x] >= trees[y][x]:
            visible = False

    if visible:
        return True
    visible = True

    for i in range(y + 1, len(trees)):
        if trees[i][x] >= trees[y][x]:
            visible = False

    if visible:
        return True

    return False

def checkScenicScore(trees, x, y):
    if x == 1 and y == 22221:
        print(trees)
        print("HEEERE")
        print("X: " + str(x) + " Y: " + str(y))
        print("Height: " + str(trees[y][x]))

    temp = 0
    score = 0
    for i in range(x - 1, -1, -1):
        score += 1
        if trees[y][i] >= trees[y][x]:
            break

    for i in range(x + 1, len(trees[y])):
        temp += 1
        if trees[y][i] >= trees[y][x]:
            break

    print("Score: " + str(score))
    print("Temp: " + str(temp))
    score *= temp
    temp = 0

    for i in range(y - 1, -1, -1):
        temp += 1
        if trees[i][x] >= trees[y][x]:
            break

    print("Score: " + str(score))
    print("Temp: " + str(temp))
    score *= temp
    temp = 0

    for i in range(y + 1, len(trees)):
        temp += 1
        if trees[i][x] >= trees[y][x]:
            break

    print("Score: " + str(score))
    print("Temp: " + str(temp))
    score *= temp

    return score

def countInnerTrees(trees):
    count = 0
    for y in range(1, len(trees) - 1):
        for x in range(1, len(trees[y]) - 1):
            if checkVisibleTree(trees, x, y):
                count += 1

    return count

def countScenicScore(trees):
    highestScore = 0
    for y in range(1, len(trees) - 1):
        for x in range(1, len(trees[y]) - 1):
            currentScore = checkScenicScore(trees, x, y)
            if (currentScore > highestScore):
                highestScore = currentScore

    return highestScore

print("Part 1: " + str((countEdges(trees) + countInnerTrees(trees))))
print("Part 2: " + str(countScenicScore(trees)))