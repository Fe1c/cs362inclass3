import unittest
import pytest
import palindrome

class TestCase(unittest.TestCase):
    #pass cases
    def test_pass_1(self):
        self.assertEqual(palindrome.palindrome("level"), 1)
    def test_pass_2(self):
        self.assertEqual(palindrome.palindrome("help"), 0)
    #fail cases
    def test_fail_1(self):
        self.assertEqual(palindrome.palindrome("racecar"), 0)
    def test_fail_2(self):
        self.assertEqual(palindrome.palindrome("value"), 1)

def test_pass():
  assert palindrome.palindrome("civic") == 1
  
def fail_test():
  assert palindrome.palindrome("good") == 1

if __name__ == '__main__':
    unittest.main()