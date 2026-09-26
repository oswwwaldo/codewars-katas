def solution(number):
    if (number < 0): return 0
​
    sum = 0
    common_multiples = []
    
    for i in range(0, number):
        if i % 3 == 0 or i % 5 == 0:
            if i not in common_multiples:
                sum += i
            
            if i % 3 == 0 and i % 5 == 0:
                common_multiples.append(i)
            
    return sum
  