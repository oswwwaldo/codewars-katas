def alphabet_position(text):
    alphabet: str = 'abcdefghijklmnopqrstuvwxyz'
    output: str = ''
    for char in text:
        if char.isalpha():
            output = output + (str(alphabet.index(char.lower()) + 1) + ' ')
        
    return output.rstrip()