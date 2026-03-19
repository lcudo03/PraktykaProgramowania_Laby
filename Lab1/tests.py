from string_calculator import Add
import unittest

class TestMyMethod(unittest.TestCase):
    def test_isNull(self):
        self.assertEqual(0, Add(""))
    def test_singleNumber(self):
        self.assertEqual(1, Add("1"))
    def test_simpleSum(self):
        self.assertEqual(3, Add("1,2"))
    def test_multiSum(self):
        self.assertEqual(6, Add("1,2,3"))
    def test_valueError(self):
        with self.assertRaises(ValueError):
            Add("1,a")
    def test_separators(self):
        self.assertEqual(5, Add("1,2\n2"))
    def test_separatorAtTheEnd(self):
        with self.assertRaises(ValueError):
            Add("1,2\n3,4\n")
    def test_doubleComma(self):
        with self.assertRaises(ValueError):
            Add("1,2\n,3,4")