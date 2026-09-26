def score(dice):
    final_score = 0
    arr = dice.copy()
    arr.sort()
​
    i = 0
    while i <= len(arr) - 3:
        triplet = arr[i:i+3]
        if triplet[0] == triplet[1] == triplet[2]:
            val = triplet[0]
            if val == 1:
                final_score += 1000
            elif val == 5:
                final_score += 500
            else:
                final_score += val * 100
​
            del arr[i:i+3]
        else:
            i += 1
​
    for num in arr:
        if num == 1:
            final_score += 100
        elif num == 5:
            final_score += 50
​
    return final_score