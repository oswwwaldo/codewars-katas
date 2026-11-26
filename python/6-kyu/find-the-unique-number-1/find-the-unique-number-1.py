def find_uniq(xs: list[int]):
    num_set = set(xs)
    for num in num_set:
        if xs.count(num) == 1:
            return num
    return 0