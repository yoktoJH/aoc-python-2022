def compare_int(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left == right:
            return None
        return left < right

    if isinstance(left, list) and isinstance(right, list):
        return compare_list(left, right)

    if isinstance(left, list):
        return compare_list(left,[right])
    return compare_list([left],right)


def compare_list(left, right):
    if len(left) < len(right):
        for i in range(len(left)):
            if compare_int(left[i], right[i]) is None:
                continue
            return compare_int(left[i], right[i])
        return True
    if len(right) < len(left):
        for i in range(len(right)):
            if compare_int(left[i], right[i]) is None:
                continue
            return compare_int(left[i], right[i])
        return False
    #len(right) == len(left)
    for i in range(len(left)):
        if compare_int(left[i], right[i]) is None:
            continue
        return compare_int(left[i], right[i])
    return None


with open("vstup.txt") as vstup:
    score = 0
    for i, line1 in enumerate(vstup):
        line2 = vstup.readline()
        empty = vstup.readline()
        sline1 = eval(line1.rstrip())
        sline2 = eval(line2.rstrip())
        if compare_list(sline1, sline2):
            print(i+1)
            score += i+1
print(score)
