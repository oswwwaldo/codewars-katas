def generate_hashtag(s):
    if (len(s) == 0): return False
​
    hashtag = "#"
    string = ""
    str = " ".join(s.split())
    lazy_index_padding = " "
    
    text = lazy_index_padding + str
​
    for index, char in enumerate(text):
        if index == 0: pass
        else:
            prevChar = text[index-1]
            if (prevChar == " "):
                print("Detected capitalized case")     
                string += char.upper()
            else:
                string += char.lower()
    
    print(string)
    result = hashtag + string.replace(" ", "")
    
    if (len(result) > 140):
        return False
    else:
        return result
    
    
​