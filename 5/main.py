def readfile(f):
    with open(f, "r") as io:
        lines = [x.replace("\n", "") for x in io.readlines()]
    split_idx = lines.index("")
    page_ordering = lines[:split_idx]
    page_numbers = [
        list(map(int, x.split(","))) for x in lines[split_idx + 1:]
    ]
    return page_ordering, page_numbers


def p1(f):
    page_ordering, page_numbers = readfile(f)
    page_ordering = [[int(p) for p in page.split("|")]
                     for page in page_ordering]
    rules = dict()
    for po in page_ordering:
        rules.setdefault(po[0], []).append(po[1])

    is_row_valid = []
    for row in page_numbers:
        for i in range(len(row) - 1):
            row_is_valid = True
            curr = row[i]
            remainder = row[i + 1:]
            for item in remainder:
                if item not in rules.get(curr, []):
                    row_is_valid = False
                    break
            if not row_is_valid:
                break
        is_row_valid.append(row_is_valid)

    middle_pages = []
    for valid_row, row in zip(is_row_valid, page_numbers):
        if valid_row:
            assert len(row) % 2 == 1
            middle_pages.append(row[len(row) // 2])

    return sum(middle_pages)


def fix_row(row, rules):
    row_is_valid = True
    for i in range(len(row) - 1):
        curr = row[i]
        remainder = row[i + 1:]
        for ii, item in enumerate(remainder):
            if item not in rules.get(curr, []):
                item_index = ii + i + 1
                row[i] = row[item_index]
                row[item_index] = curr
                row_is_valid = False
                break

        if not row_is_valid:
            break

    if row_is_valid:
        return row
    else:
        return fix_row(row, rules)


def p2(f):
    page_ordering, page_numbers = readfile(f)
    page_ordering = [[int(p) for p in page.split("|")]
                     for page in page_ordering]
    rules = {}
    for po in page_ordering:
        rules.setdefault(po[0], []).append(po[1])

    is_row_valid = []
    for row in page_numbers:
        for i in range(len(row) - 1):
            row_is_valid = True
            curr = row[i]
            remainder = row[i + 1:]
            for item in remainder:
                if item not in rules.get(curr, []):
                    row_is_valid = False
                    break
            if not row_is_valid:
                break
        is_row_valid.append(row_is_valid)

    inverted_rules = {}
    for key, values in rules.items():
        for value in values:
            inverted_rules.setdefault(value, []).append(key)

    middle_pages = []
    for valid_row, row in zip(is_row_valid, page_numbers):
        if not valid_row:
            assert len(row) % 2 == 1
            new_row = fix_row(row, rules)
            middle_pages.append(new_row[len(new_row) // 2])

    return sum(middle_pages)


print(p1("t1.txt"))
print(p1("input.txt"))
print(p2("t1.txt"))
print(p2("input.txt"))
