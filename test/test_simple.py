from unittest import TestCase #, main
from simple_eg import suma, es_mayor, es_igual

class TestDatabaseFunctions(TestCase):

    def test_suma(self):
        self.assertEqual(suma(2, 2), 4)
    
    def test_es_mayor(self):
        self.assertEqual(es_mayor(4, 3), True)
    
    def test_es_igual(self):
        self.assertEqual(es_igual(5, 5), True)