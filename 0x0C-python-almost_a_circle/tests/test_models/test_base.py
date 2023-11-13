#!/usr/bin/python3
"""base testing"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Test_Base(unittest.TestCase):
    """class tester for base"""

    def setUp(self):
        """seting up"""
        Base._Base__nb_objects = 0
        pass

    def tearDown(self):
        """reset the value"""
        pass

    def test_simple(self):
        """simple test"""
        b1 = Base()
        b2 = Base(15)
        b3 = Base()
        self.assertEqual(b3.id, 2)

    def test_simple2(self):
        """simple test 2"""
        b = Base(33)
        c = Base()
        self.assertEqual(b.id + c.id, 34)

    def test_type(self):
        """testing type"""
        b1 = Base()
        self.assertEqual(str(type(b1)), "<class 'models.base.Base'>")

    def test_arg(self):
        """testing missing args"""
        with self.assertRaises(TypeError):
            Base.__init__()

    def test_arg2(self):
        """testing extra arg"""
        with self.assertRaises(TypeError):
            b = Base(1, 2)

    def test_int(self):
        a = 55
        b = Base(a)
        self.assertEqual(b.id, a)

    def test_arg3(self):
        """test equality between class and instance"""
        b = Base()
        b = Base()
        b = Base(14)
        b = Base()
        self.assertEqual(getattr(Base, "_Base__nb_objects"), b.id)

    def test_arg4(self):
        """testing string"""
        b = Base("hello")
        self.assertEqual(b.id, "hello")

if __name__ == "__main__":
    unittest.main()
