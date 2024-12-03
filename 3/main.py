import re


def readfile(f):
    with open(f, "r") as io:
        return io.read().split("\n")[0]



def p1(f):
    text = readfile(f)
    result = []
    i = 0
    while i < len(text):
        if text[i:i + 4] == "mul(":
            close_paren_index = (text.find(")", i + 4))
            if close_paren_index == -1:
                break
            contents = text[i+4:close_paren_index]
            contents_split = contents.split(",")
            if len(contents_split) != 2:
                i+=1
                continue
            try:
                items = [int(x) for x in contents_split]
                result.append(items[0] * items[1])

            except ValueError:
                i += 1
        i += 1
    return sum(result)


def p2(f):
    text = readfile(f)
    result = []
    dont = False
    i = 0
    while i < len(text):
        if text[i:i+7] == "don't()":
            dont = True
        if text[i:i+4] == "do()":
            dont = False
        if dont:
            i += 1
            continue
        if text[i:i + 4] == "mul(":
            close_paren_index = (text.find(")", i + 4))
            if close_paren_index == -1:
                break
            contents = text[i+4:close_paren_index]
            contents_split = contents.split(",")
            if len(contents_split) != 2:
                i+=1
                continue
            try:
                items = [int(x) for x in contents_split]
                result.append(items[0] * items[1])

            except ValueError:
                i += 1
        i += 1
    return sum(result)



print(p1("t1.txt"))
print(p1("input.txt"))
print(p2("t2.txt"))
print(p2("input.txt"))
