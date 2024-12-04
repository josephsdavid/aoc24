import itertools as it
import numpy as np
def readfile(f):
    with open(f, "r") as io:
        return [[xi for xi in x] for x in io.read().split("\n") if len(x) > 0]



def p1(f):
    data = np.array(readfile(f))
    is_x = data == "X"
    is_m = data == "M"
    is_a = data == "A"
    is_s = data == "S"
    good_indices = []
    directions = it.product([0, 1, -1], repeat=2)
    directions = [d for d in directions if d != (0, 0)]

    def check_direction(direction, i, j):
        dx, dy = direction
        indices = []
        for arr_idx, arr in enumerate([is_x, is_m, is_a, is_s]):
            try:
                test_idx = (i + dx * arr_idx, j + dy * arr_idx)
                if test_idx[0] < 0:
                    return []
                if test_idx[1] < 0:
                    return []

                if not arr[test_idx[0], test_idx[1]]:
                    return []
                indices.append(test_idx)
            except IndexError:
                return []

        return set(indices)

    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            for direction in directions:
                indices = check_direction(direction, i, j)
                if indices:
                    good_indices.append(indices)
    return len(good_indices)



def p2(f):
    data = np.array(readfile(f))
    is_a = data == "A"

    count = 0

    def check_center(i, j):
        if i == 0 or j == 0 or i == (data.shape[0] - 1) or j == (data.shape[-1] - 1):
            return False
        square = data[i - 1:i + 2, j - 1:j + 2]
        square = np.where(square == 'M', 1, np.where(square == 'S', -1, 0))
        corners = square[[0, 0, 2, 2], [0, 2, 0, 2]]
        if not np.all(np.isin(corners, [-1, 1])):
            return False
        if not (corners[0] == -corners[3] and corners[1] == -corners[2]):
            return False
        return True

    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            if not is_a[i, j]:
                continue
            try:
                if check_center(i, j):
                    count += 1
            except IndexError:
                continue


    return count

if __name__ == "__main__":
    print(p1("t1.txt"))
    print(p1("input.txt"))
    print(p2("t1.txt"))
    print(p2("input.txt"))

