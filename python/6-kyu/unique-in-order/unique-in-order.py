def unique_in_order(sequence):        
    unique = []
    previous_item = None
    
    for item in sequence: 
        if item not in unique:
            unique.append(item)
            previous_item = item
        elif item in unique:
            if previous_item == item:   
                pass
            else:
                unique.append(item)
                previous_item = item
    return unique