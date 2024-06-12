from db.connection import app
from unittest import TestCase #, main
from calls import isEmpl, isCustomer, cantVent

class TestDatabaseFunctions(TestCase):
    def setUp(self):
        self.app = app.test_client()
    
    def test_isEmpl(self):
        self.assertEqual(isEmpl('Juan'), True)
    
    def test_isCustomer(self):
        self.assertEqual(isCustomer('Juan'), False)
    
    def test_cantVent(self):
        self.assertEqual(cantVent('Juan'), 10)
    