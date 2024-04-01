from unittest import TestCase#, main
from db.consultas import add_cliente, add_empleado, add_venta

class TestDatabaseFunctions(TestCase):
    def test_add_empleado(self):
        id = add_empleado("Juan")
        self.assertIsNotNone(id, "Failed to add employee")

    def test_add_cliente(self):
        id = add_cliente("Carlos")
        self.assertIsNotNone(id, "Failed to add client")

    def test_add_venta(self):
        id_empleado = add_empleado("Juan")
        id = add_venta("Arroz", id_empleado)
        self.assertIsNotNone(id, "Failed to add sale")

def prueba_test():
    print('si testea')

#if __name__ == '__main__':
#    main()
