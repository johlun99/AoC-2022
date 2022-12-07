with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

currentPath = "/"
dirs = {}

def navigate(commandParts, currentPath):
    if commandParts[1] == "cd":
        if commandParts[2] == "/":
            currentPath = "/"
        elif commandParts[2] == "..":
            currentPath = currentPath.split("/")[:-2]
            currentPath = "/".join(currentPath) + "/"
        else:
            currentPath += parts[2] + "/"

    return currentPath


def getDir(lines, index):
    dir = []
    while True:
        index += 1
        if index >= len(lines) or lines[index][0] == "$":
            #print(lines[index])
            break

        dir.append(lines[index])
    
    return dir


def getDirSizeRecursive(dirs, currentDir):
    size = 0
    for line in dirs[currentDir]:
        parts = line.split(" ")
        if parts[0].isdigit():
            size += int(parts[0])
        elif parts[0] == "dir":
            size += getDirSizeRecursive(dirs, currentDir + parts[1] + "/")
        else:
            print("Unexpected line:")
            print(line)
            exit()
    return size


def summerizeSizes(dirSizes):
    for key in dirSizes:
        size = dirSizes[key]
        for k in dirSizes:
            if key in k:
                size += dirSizes[k]

        dirSizes[key] = size

    return dirSizes


for i in range(len(lines)):
    parts = lines[i].split(" ")
    if parts[0] == '$':
        if parts[1] == "cd":
            currentPath = navigate(parts, currentPath)

        if parts[1] == "ls":
            dirs[currentPath] = getDir(lines, i)


dirSizes = {}
for key in dirs:
    dirSizes[key] = getDirSizeRecursive(dirs, key)

part1 = 0
for key in dirSizes:
    if dirSizes[key] <= 100000:
        part1 += dirSizes[key]

closestDir = {"dir": '/', "size": dirSizes['/']}
spaceToFree = 6233734

for key in dirSizes:
    if dirSizes[key] > spaceToFree and dirSizes[key] < closestDir["size"]:
        closestDir["dir"] = key
        closestDir["size"] = dirSizes[key]

print("part 1: " + str(part1))
print("Part 2: " + str(closestDir["size"]))