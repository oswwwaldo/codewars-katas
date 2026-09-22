def tribonacci(signature, n):
    if (n == 0): return []
    
    range = n
    bound = 0
    
    while(range > 0):
        signature.append(sum(signature[bound:]));
        bound += 1
        range -= 1
        
    return signature[:n]