#!/usr/bin/python3
"""base class test file"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Base class for testing"""

    def test_Base(self):
        """tests for the base class"""

        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base(20)
        self.assertEqual(b2.id, 20)
        b3 = Base()
        self.assertEqual(b3.id, 2)


if __name__ == '__main__':
    unittest.main()
