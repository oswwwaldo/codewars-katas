def square_digits(num):
    output: str = ""
    
    for i in str(num):
        output = output + str(int(i) ** 2)
        
    return int(output)