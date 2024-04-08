from db.connection import app, mysql
from unittest import TestCase , main
from db.consultas import add_cliente, add_empleado, add_venta, prod_vendidos

class TestDatabaseFunctions(TestCase):
    def setUp(self):
        self.app = app.test_client()
        
    def test_prod_vendidos(self):
        self.assertEqual(prod_vendidos('1'), 10)
        self.assertEqual(prod_vendidos('2'), 8)
        self.assertEqual(prod_vendidos('3'), 3)
        self.assertEqual(prod_vendidos('5'), 1)
    
'''
    def test_add_empleado(self):
        with app.app_context():
            add_empleado('Javier')
            cur = mysql.connection.cursor()
            result = cur.execute("SELECT * FROM empleados WHERE nombre = 'Javier'")
            self.assertEqual(result, 1)

    def test_add_cliente(self):
        with app.app_context():
            add_cliente('Pedro')
            cur = mysql.connection.cursor()
            result = cur.execute("SELECT * FROM clientes WHERE nombre = 'Pedro'")
            self.assertEqual(result, 1)

    def test_add_venta(self):
        with app.app_context():
            add_venta('Producto X', 1)
            cur = mysql.connection.cursor()
            result = cur.execute("SELECT * FROM ventas WHERE producto = 'Producto X' AND id_empleado = 1")
            self.assertEqual(result, 1)

'''


#if __name__ == '__main__':
#    main()
