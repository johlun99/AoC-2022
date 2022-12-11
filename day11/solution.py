import time
from copy import deepcopy

START_TIME= time.time()
data = open("input.txt", "r").read().strip()
lines = [x for x in data.split('\n')]

ITEMS = []
OPERATIONS = []
DIVISIBLES = []
IS_TRUE = []
IS_FALSE = []
for monkey in data.split('\n\n'):
    id_, items, op, test, is_true, is_false = monkey.split('\n')
    ITEMS.append([int(i) for i in items.split(':')[1].split(',')])
    words = op.split()
    op = ''.join(words[-3:])
    OPERATIONS.append(lambda old,op=op:eval(op))
    DIVISIBLES.append(int(test.split()[-1]))
    IS_TRUE.append(int(is_true.split()[-1]))
    IS_FALSE.append(int(is_false.split()[-1]))

START = deepcopy(ITEMS)

lcm = 1
for x in DIVISIBLES:
    lcm = (lcm*x)

for part in [1,2]:
    C = [0 for _ in range(len(ITEMS))]
    ITEMS = deepcopy(START)
    for t in range(20 if part==1 else 10000):
        for i in range(len(ITEMS)):
            for item in ITEMS[i]:
                #print(i,item)
                C[i] += 1
                item = OPERATIONS[i](item)
                if part == 2:
                    item %= lcm

                if part == 1:
                    item = (item // 3)
                if item % DIVISIBLES[i] == 0:
                    ITEMS[IS_TRUE[i]].append(item)
                else:
                    ITEMS[IS_FALSE[i]].append(item)
            ITEMS[i] = []

    if part == 1:
        print("Part 1")

    else:
        print("Part 2")

    print(sorted(C)[-1] * sorted(C)[-2])

print("Execution time: " + str(time.time() - START_TIME))