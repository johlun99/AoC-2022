with open("example-input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

def getScore(move):
    parts = move.split(" ")

    if parts[0] == 'A':
        if parts[1] == 'X':
            return 4
        elif parts[1] == 'Y':
            return 8
        elif parts[1] == 'Z':
            return 3
    elif parts[0] == 'B':
        if parts[1] == 'X':
            return 1
        elif parts[1] == 'Y':
            return 5
        elif parts[1] == 'Z':
            return 9
    elif parts[0] == 'C':
        if parts[1] == 'X':
            return 7
        elif parts[1] == 'Y':
            return 2
        elif parts[1] == 'Z':
            return 6

score = 0
for move in lines:
    score += getScore(move)

print("Part 1: " + str(score))
