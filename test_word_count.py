# Word Count Unittest
# By: Jason Graalum
import unittest
import word_count

class test_wordcount(unittest.TestCase):
    def test_true1(self):
        self.assertEqual(word_count.count("To be or not to be"), 6)
    def test_true2(self):
        self.assertEqual(word_count.count(""), 0)
    def test_true3(self):
        self.assertEqual(word_count.count("Hello there"), 2)
        
    def test_false1(self):
        self.assertNotEqual(word_count.count("Hello"), 2)
    def test_false2(self):
        self.assertNotEqual(word_count.count("All the worlds a stage"), 6)
    def test_false3(self):
        self.assertNotEqual(word_count.count("Me Myself and I"), 3)

if __name__ == '__main__':
    unittest.main()

