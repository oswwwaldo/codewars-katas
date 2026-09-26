def create_phone_number(n):
    open = "("
    close = ")"
    space = " "
    dash = "-"
    beginning = ""
    middle = ""
    end = ""
    
    for index, num in enumerate(n):
        if index < 3:
            beginning += str(num)
        elif index < 6:
            middle += str(num)
        else:
            end += str(num)
        
    return open + beginning + close + space + middle + dash + end