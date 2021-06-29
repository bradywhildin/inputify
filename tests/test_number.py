## To run these tests, run 'python -m unittest discover' in directory containing inputify/ and tests/

import unittest
from unittest.mock import patch

from inputify.number import BadFunctionError, BadInputError, validateNum, getNum

class TestNumber(unittest.TestCase):
    def test_accept_int(self):
        self.assertTrue(validateNum(1))

    def test_accept_float(self):
        self.assertTrue(validateNum(1.11))

    def test_raise_if_input_is_not_num(self):
        self.assertRaises(TypeError, validateNum, '1')

    def test_raise_if_min_is_not_number(self):
        self.assertRaises(TypeError, validateNum, 1, max='2')

    def test_raise_if_validator_is_not_function(self):
        with self.assertRaises(TypeError) as context:
            validateNum(1, validator=1)
        self.assertEqual('validator must be of type function', str(context.exception))

    def test_raise_if_validator_does_not_have_one_parameter(self):
        validator = lambda a,b : a + b
        with self.assertRaises(BadFunctionError) as context:
            validateNum(1, validator=validator)
        self.assertEqual('validator must have one parameter', str(context.exception))

    def test_raise_if_validator_does_not_return_bool(self):
        validator = lambda a : 1
        with self.assertRaises(BadFunctionError) as context:
            validateNum(1, validator=validator)
        self.assertEqual('validator must return a value of type bool', str(context.exception))

    def test_reject_num_too_small(self):
        self.assertFalse(validateNum(-5, min=-4))

    def test_reject_num_too_big(self):
        self.assertFalse(validateNum(24, max=23))

    def test_accept_num_that_meets_validator(self):
        validator = lambda x : x % 2 == 0
        self.assertTrue(validateNum(4, validator=validator))

    def test_reject_num_that_fails_validator(self):
        validator = lambda x : x % 2 == 0
        self.assertFalse(validateNum(3, validator=validator))

    # side_effect is list of values that will be given to input() calls
    @patch('builtins.input', side_effect=['1'])
    def test_get_num(self, mock_input):
        self.assertEqual(getNum(), 1)

    @patch('builtins.input', side_effect=['a', '2.1', '3', '-5', '-10', '6', '-2', '2'])
    def test_get_num_with_partly_bad_input(self, mock_input):
        validator = lambda x : x % 2 == 0
        self.assertEqual(getNum(errMsg='', validator=validator, min=-8, max=4), -2)

    @patch('builtins.input', side_effect=['1', '2', '5', '6', '3'])
    def test_raise_when_too_many_tries(self, mock_input):
        self.assertRaises(BadInputError, getNum, errMsg='', maxTries=4, min=3, max=4)

if __name__ == '__main__':
    unittest.main()