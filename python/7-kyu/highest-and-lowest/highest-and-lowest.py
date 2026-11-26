def high_and_low(numbers):
    ints = [int(num) for num in numbers.split(' ')]
    return f"{max(ints)} {min(ints)}"