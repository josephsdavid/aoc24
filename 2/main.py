import numpy as np

def readfile(f):
    with open(f, "r") as io:
        data =  [x for x in io.read().split("\n") if len(x) > 0]
        return [[int(xi) for xi in x.split()] for x in data]


def is_safe(row):
        arr = np.array(row)
        diffs = np.diff(arr)
        if np.max(np.abs(diffs)) > 3:
            return False
        signs = np.sign(diffs)
        if not np.all(signs == signs[0]):
            return False
        if np.any(diffs == 0):
            return False
        return True

def p1(f):
    safe = 0
    for row in readfile(f):
        if not is_safe(row):
            continue
        safe += 1
    return safe


def p2(f):
    safe = 0
    for row in readfile(f):
        if is_safe(row):
            safe += 1
            continue
        for exclude in range(len(row)):
            dropped_row = [item for i, item in enumerate(row) if i != exclude]
            if is_safe(dropped_row):
                safe += 1
                break
        continue

    return safe


print(p1("t1.txt"))
print(p1("input.txt"))
print(p2("t1.txt"))
print(p2("input.txt"))
