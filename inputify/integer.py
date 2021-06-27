from inspect import signature

class BadFunctionError(TypeError):
    pass

def validateInt(input, validator=lambda x:True, min=float('-inf'), max=float('inf')):
    if not isinstance(input, int):
        raise TypeError('input must be of type int')

    try:
        validatorPass = validator(input)
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
        withinRange = input >= min and input <= max
    except TypeError:
        raise TypeError('min and max must be of type int or float')
        
    return validatorPass and withinRange