from inspect import signature

class BadFunctionError(TypeError):
    pass

def validateNum(inp, validator=lambda x:True, min=float('-inf'), max=float('inf')):
    if not isinstance(inp, int) and not isinstance(inp, float):
        raise TypeError('inp must be of type int or float')

    try:
        validatorPass = validator(inp)
    except TypeError as e:
        if not callable(validator):
            raise TypeError('validator must be of type function')
        elif len(signature(validator).parameters) != 1:
            raise BadFunctionError('validator must have one parameter')
        else:
            raise e

    if not isinstance(validatorPass, bool):
        raise BadFunctionError('validator must return a value of type bool')

    try:
        withinRange = inp >= min and inp <= max
    except TypeError:
        raise TypeError('min and max must be of type int or float')
        
    return validatorPass and withinRange

class BadInputError(Exception):
    pass

def getNum(prompt='Enter number: ', errMsg='Invalid input', maxTries=10, validator=lambda x:True, min=float('-inf'), max=float('inf')):
    for _ in range(maxTries):
        inp = input(prompt)
        try:
            inp = float(inp)
        except:
            print(errMsg)
            continue

        if validateNum(inp, validator, min, max):
            return inp
        else:
            print(errMsg)
    
    raise BadInputError('Max number of tries exceeded')
