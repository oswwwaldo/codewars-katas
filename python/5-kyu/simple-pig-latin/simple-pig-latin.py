def pig_it(text):
    
    result = ""
​
    for index, word in enumerate(text.split()):
        if word.isalpha():
            result += word[1:] + word[0] + "ay"
            
            if index == len(text.split()) - 1:
                pass
            else:
                result += " "
        else:
            result += word
    
    return result
#     return result[:len(result) - 1]
​