from collections import deque
from copy import deepcopy

data = open("input.txt", "r").read().strip()
lines = [row for row in data.split("\n")]

MAP = []
for line in lines:
    MAP.append(line)

HEIGHT = len(MAP)
WIDTH = len(MAP[0])

E = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]
for r in range(HEIGHT):
    for c in range(WIDTH):
        if MAP[r][c] == "S":
            E[r][c] = 1
        elif MAP[r][c] == "E":
            E[r][c] = 26
        else:
            E[r][c] = ord(MAP[r][c]) - ord("a") + 1

def solve(part):
    queue = deque()
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if (part == 1 and MAP[y][x] == 'S') or (part == 2 and E[y][x] == 1):
                queue.append(((y, x), 0))
    
    my_set = set()
    while queue:
        (y, x), d = queue.popleft()
        if (y, x) in my_set:
            continue

        my_set.add((y, x))

        if MAP[y][x] == 'E':
            return d
        
        for dy, dx in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            yy = y + dy
            xx = x + dx

            if 0 <= yy < HEIGHT and 0 <= xx < WIDTH and E[yy][xx] <= 1 + E[y][x]:
                queue.append(((yy, xx), d + 1))

print("Part 1: " + str(solve(1)))
print("Part 2: " + str(solve(2)))
