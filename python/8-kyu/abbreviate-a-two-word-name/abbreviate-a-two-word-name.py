def abbrev_name(name):
    result = "";
    names = name.split(" ")
​
    for name in names:
        result += name[0:1].upper()
        if (names[0] == name):
            result+= "."
        
        
    return result;