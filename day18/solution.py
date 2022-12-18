import numpy as np
from functools import lru_cache
from tqdm import tqdm

with open("input.txt", "r") as f:
    lines = [i.strip().split(',') for i in f.readlines()]
    data = []
    for l in lines:
        data.append([int(i) for i in l])


def compareAdj(c1, c2):
    countSame = 0
    for s in range(3):
        if c1[s] == c2[s]:
            countSame += 1

        elif c1[s] < c2[s] - 1 or c1[s] > c2[s] + 1:
            return 0

    if countSame == 2:
        return 1

    return 0


countCovered = 0
for i in range(len(data) - 1):
    for j in range(i + 1, len(data)):
        countCovered += compareAdj(data[i], data[j])

p1 = (6 * len(data)) - (countCovered * 2)
print("Part 1: " + str(p1))

min_coord = 1 << 60
max_coord = -(1 << 60)

filled = set()
for l in data:
    x, y, z = l
    filled.add((x, y, z))

    for num in [x, y, z]:
        min_coord = min(min_coord, int(num))
        max_coord = max(max_coord, int(num))


@lru_cache(None)
def exposed(pos):
    # do a DFS
    stack = [pos]
    seen = set()

    if pos in filled:
        return False

    while len(stack) > 0:
        pop = stack.pop()

        if pop in filled:
            continue

        for coord in range(3):
            if not (min_coord <= pop[coord] <= max_coord):
                return True

        if pop in seen:
            continue
        seen.add(pop)

        for coord in range(3):
            dpos = np.array([0, 0, 0])
            dpos[coord] = 1
            dneg = np.array([0, 0, 0])
            dneg[coord] = -1

            stack.append(tuple(pop + dpos))
            stack.append(tuple(pop + dneg))

    return False


ans = 0
for x, y, z in tqdm(filled):
    covered = 0

    pos = np.array((x, y, z))

    for coord in range(3):
        dpos = np.array([0, 0, 0])
        dpos[coord] = 1

        dneg = np.array([0, 0, 0])
        dneg[coord] = -1

        for nbr in [tuple(pos + dpos), tuple(pos + dneg)]:
            ans += exposed(nbr)


print("Part 2: " + str(ans))