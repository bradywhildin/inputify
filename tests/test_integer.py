import unittest

from inputify.integer import BadFunctionError, validateInt

class TestInteger(unittest.TestCase):
    def test_accept_int(self):
        self.assertTrue(validateInt(1))

    def test_raise_if_input_is_not_int(self):
        self.assertRaises(TypeError, validateInt, 1.1)

    def test_raise_if_min_is_not_number(self):
        self.assertRaises(TypeError, validateInt, 1, max='2')

    def test_raise_if_validator_is_not_function(self):
        with self.assertRaises(TypeError) as context:
            validateInt(1, validator=1)
        self.assertEqual('validator must be of type function', str(context.exception))

    def test_raise_if_validator_does_not_have_one_parameter(self):
        validator = lambda a,b : a + b
        with self.assertRaises(BadFunctionError) as context:
            validateInt(1, validator=validator)
        self.assertEqual('validator must have one parameter', str(context.exception))

    def test_raise_if_validator_does_not_have_one_parameter(self):
        validator = lambda a : 1
        with self.assertRaises(BadFunctionError) as context:
            validateInt(1, validator=validator)
        self.assertEqual('validator must return a value of type bool', str(context.exception))

    def test_reject_int_too_small(self):
        self.assertFalse(validateInt(-5, min=-4))

    def test_reject_int_too_big(self):
        self.assertFalse(validateInt(24, max=23))

    def test_accept_int_that_meets_validator(self):
        validator = lambda x : x % 2 == 0
        self.assertTrue(validateInt(4, validator=validator))

    def test_reject_int_that_fails_validator(self):
        validator = lambda x : x % 2 == 0
        self.assertFalse(validateInt(3, validator=validator))