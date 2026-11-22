def same_structure_as(original, other):   
    if isinstance(original, list) != isinstance(other, list): return False
    if not isinstance(original, list): return True
    if len(original) != len(other): return False
        
    # recursively check every paired element
    return all(same_structure_as(a, b) for a, b in zip(original, other))
    
    
#     return len(original) == len(other) # passed 103 cases, failed 7 lol 