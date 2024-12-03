import heapq
from collections import Counter
def readfile(f):
    with open(f, "r") as io:
        return [x for x in io.read().split("\n") if len(x) > 0]

x = readfile("t1.txt")

def part1(f):
    lines = readfile(f)
    l1, l2 = map(lambda x: [int(xi) for xi in x], list(zip(*[x.split() for x in lines])))


    heapq.heapify(l1)
    heapq.heapify(l2)
    distances = []
    while l1:
        distance = heapq.heappop(l1) - heapq.heappop(l2)
        distances.append(abs(distance))
    return sum(distances)


def part2(f):
    lines = readfile(f)
    l1, l2 = map(lambda x: [int(xi) for xi in x], list(zip(*[x.split() for x in lines])))
    counts = Counter(l2)
    distances = []
    for item in l1:
        item_count = counts.get(item, 0)
        distances.append(item * item_count)


    return sum(distances)





assert part1("t1.txt") == 11
print(part1("input.txt"))
assert part2("t1.txt") == 31
print(part2("input.txt"))
