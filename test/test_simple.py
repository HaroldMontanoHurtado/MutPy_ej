from unittest import TestCase #, main
from simple_eg import suma, resta

class TestDatabaseFunctions(TestCase):

    def test_suma(self):
        self.assertEqual(suma(2, 2), 4)
    
    def test_rest(self):
        self.assertEqual(resta(4, 2), 2)