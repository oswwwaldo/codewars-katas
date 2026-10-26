def digitize(n):
    output = []
    number = str(n)
    for digit in number:
        output.insert(0, int(digit))
    return output