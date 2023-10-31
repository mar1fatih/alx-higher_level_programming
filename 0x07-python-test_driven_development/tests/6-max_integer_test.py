#!/usr/bin/python3
"""tester for max int"""


import unittest
max_integer = __import__("6-max_integer").max_integer


class test_max_int(unittest.TestCase):

    def test_max(self):
        """simple test"""
        result = max_integer([55, 14, 13, 16])
        self.assertEqual(result, 55)

    def test_none(self):
        """test empty list"""
        result = max_integer([])
        self.assertEqual(result, None)

    def test_none2(self):
        """test no arg"""
        result = max_integer()
        self.assertEqual(result, None)

    def test_negatives(self):
        """test with negative numbers"""
        result = max_integer([-55, -14, -13, -16])
        self.assertEqual(result, -13)

    def test_floats(self):
        """test with floats numbers"""
        result = max_integer([0.51, 5.12, 6.54, 55.5, 55.6])
        self.assertEqual(result, 55.6)

    def test_string(self):
        """test string with numbers"""
        result = max_integer("14863589")
        self.assertEqual(result, "9")

    def test_lists(self):
        """test lists on list"""
        result = max_integer([[5], [6], [8], [10], [100]])
        self.assertEqual(result, [100])

    def test_int_and_float(self):
        """test ints with floats on list"""
        result = max_integer([5, 5.1, 4.9, 4])
        self.assertEqual(result, 5.1)

    def test_string_int(self):
        """testing error 1"""
        with self.assertRaises(TypeError):
            max_integer(["ki", 5])

    def test_more_arg(self):
        """testing error 2"""
        with self.assertRaises(TypeError):
            max_integer([1], [2])

    def test_none_arg(self):
        """testing error 3"""
        with self.assertRaises(TypeError):
            max_integer(None)


if __name__ == "__main__":
    unittest.main()
