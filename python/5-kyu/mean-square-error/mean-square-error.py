def solution(array_a, array_b):
    if (len(array_a) == len(array_b)):
        sum = 0
        for index, i in enumerate(array_a):
            difference = array_b[index] - array_a[index]
            sum += difference ** 2
        
        number = sum / len(array_a)
        return number
    else:
        return 0