def high(x):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    collection = {}
    words = x.split()
    for word in words:
        for letter in word:
            
            if word in collection:
                collection[word] += (alphabet.index(letter) + 1) # increment the score for that word
                print(f"{word} is now at {collection[word]} score")
            else:
                collection[word] = alphabet.index(letter) # create the item if not in collection
                print(f"{word} has been added and sits at {collection[word]} score")
    
    highest_value = max(collection, key=collection.get)
    
    return highest_value
            
    