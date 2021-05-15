# Palindrome Unittest
# By: Jason Graalum
import unittest
import palindrome

class test_palindrome(unittest.TestCase):
    def test_true1(self):
        self.assertTrue(palindrome.palindrome("Bob"))
    def test_true2(self):
        self.assertTrue(palindrome.palindrome("level"))
    def test_true3(self):
        self.assertTrue(palindrome.palindrome("RaCecAr"))
    
    def test_false1(self):
        self.assertFalse(palindrome.palindrome("hello"))
    def test_false2(self):
        self.assertFalse(palindrome.palindrome("race car"))
    def test_false3(self):
        self.assertFalse(palindrome.palindrome("llevel"))
        
if __name__ == '__main__':
    unittest.main()

