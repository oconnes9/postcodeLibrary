from unittest import TestCase
from postcode import is_valid, format, InvalidPostcodeError

class TestPostcodes(TestCase):
    def test_validation(self):
        self.assertTrue(is_valid('SW1W 0NY'))   #Tests correct value

        self.assertTrue(is_valid('L1 8JQ'))     #Tests correct value

        self.assertFalse(is_valid('sw1w 0ny'))   #Tests lowercase

        self.assertFalse(is_valid('SWTY H55'))   #Tests correct length but wrong positioning of letters/numbers

        self.assertFalse(is_valid('XX9O Y798H')) #Tests wrong length and wrong positioning of letters/numbers

    def test_formatting(self):
        self.assertEqual(format('sw1w 0ny'), 'SW1W 0NY')  #Tests lowercase

        self.assertEqual(format('sw1w0ny'), 'SW1W 0NY')   #Tests no space

        self.assertEqual(format('L18 JQ'), 'L1 8JQ')      #Tests space in wrong position


    def test_exception(self):   #Tests that exception raised when attempted to format invalid postcode
        with self.assertRaises(InvalidPostcodeError):
            format('XX9O Y798H')

        with self.assertRaises(InvalidPostcodeError):
            format('SWTY H55')

