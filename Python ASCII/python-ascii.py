def toUpper(letter):
    return chr( ord( letter) - 32)
    
def toLower(letter):
    return chr( ord( letter) + 32)
    
def isAlphabet(letter):
    asciiValue = ord(letter)
    if (asciiValue >= 65 and asciiValue <= 90) or (asciiValue >= 97 and asciiValue <= 122):
        return True
    return False
    
def isDigit(letter):
    asciiValue = ord(letter)
    if asciiValue >= 48 and asciiValue <= 57:
        return True
    return False
    
def isSpecialChar(letter):
    asciiValue = ord(letter)
    if (asciiValue >= 33 and asciiValue <= 47) or (asciiValue >= 58 and asciiValue <= 96) or (asciiValue >= 123 and asciiValue <= 126):
        return True
    return False