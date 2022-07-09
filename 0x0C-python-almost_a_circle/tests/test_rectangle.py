#!/usr/bin/python3
"""base class test file"""
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRect(unittest.TestCase):
    """Rectangle class for testing"""

    def test_id(self):
        """tests for the rectangle class"""

        Base.reset_base_obj()
        r1 = Rectangle(10, 2,)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r3.id, 12)

    def test_raises_exception(self):
        """tests for value exceptions"""

        with self.assertRaises(TypeError):
            Rectangle(2, "2")
        with self.assertRaises(ValueError):
            Rectangle(2, 2, 2, -4)
        with self.assertRaises(ValueError):
            Rectangle(2, 0)
        with self.assertRaises(TypeError, ):
            Rectangle(2, 2, '7', 7)

    def test_area(self):
        """tests for correct area calculation"""

        r1 = Rectangle(3, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r1.area(), 6)
        self.assertEqual(r2.area(), 20)
        self.assertEqual(r3.area(), 56)


if __name__ == '__main__':
    unittest.main()
