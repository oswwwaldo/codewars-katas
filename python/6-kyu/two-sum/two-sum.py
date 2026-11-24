def two_sum(numbers, target):
    for index, num in enumerate(numbers):
        for i, n in enumerate(numbers):
            if n + num == target and index != i:
                return index, i