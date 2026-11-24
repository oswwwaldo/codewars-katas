def two_sum(numbers, target):
    seen = {}
    for index, number in enumerate(numbers):
        needed = target - number
        
        if needed in seen:
            return index, seen[needed]
        
        seen[number] = index