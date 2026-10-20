def unique_in_order(sequence):        
    unique = []
    previous_item = None
    
    for item in sequence: 
        if item != previous_item:
            unique.append(item)
            previous_item = item
​
    return unique