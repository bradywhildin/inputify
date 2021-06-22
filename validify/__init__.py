def validateInt(input, min, max):
    if type(input) == int:
        num = input
    elif type(input) == str:
        if not str.isnumeric():
            return False
        num = int(input)
    else:
        return False

    return num >= min and num <= max

    
    