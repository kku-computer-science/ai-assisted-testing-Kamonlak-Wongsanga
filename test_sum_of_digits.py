import unittest
from sum_of_digits import sum_of_digits #chat gpt 
class TestSumOfDigits(unittest.TestCase):

    def test_single_digit_number1(self): #chat gpt 
        result = sum_of_digits(51)
        self.assertEqual(result, 6)

    def test_multiple_digit_number2(self): #chat gpt 
        result = sum_of_digits(493193)
        self.assertEqual(result, 2)

    def test_single_digit_number3(self): 
        result = sum_of_digits(16)
        self.assertEqual(result, 7)
    
    def test_multiple_digit_number4(self):
        result = sum_of_digits(52)
        self.assertEqual(result, 8)

    def test_multiple_digit_number5(self):
        result = sum_of_digits(493193)
        self.assertEqual(result, 1)

if __name__ == '__main__': #chat gpt 
    unittest.main() 
