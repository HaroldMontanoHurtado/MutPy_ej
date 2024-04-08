import unittest
from example.simple import Simple


class SimpleGoodTest(unittest.TestCase):

    def setUp(self):
        self.simple = Simple(1337)

    def test_add(self):
        self.assertEqual(self.simple.add(2, 2), 4)

    def test_add_two(self):
        self.assertEqual(self.simple.add_two(2), 4)

    def test_add_etc(self):
        self.assertEqual(self.simple.add_etc('ala, kot, pies'), 'ala, kot, pies etc.')
