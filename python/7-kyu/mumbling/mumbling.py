def accum(st):
    chars = list(st.upper())
    
    output = ""
    for index, char in enumerate(chars):
        output += char.upper()
    
        for i in range(index):
            output += char.lower()
​
        if (index == len(st) - 1):
            return output
        else: 
            output += "-"
    return output