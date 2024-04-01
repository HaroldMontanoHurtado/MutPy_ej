from db.consultas import *
from test.test_crud import *

print(' - - - - CRUD - - - -')
print('1. Añadir empleados.')
print('2. Añadir cliente.')
print('3. Añadir ventas.')
print('4. Reporte de ventas.')

text = int(input('Digite: '))

if (text==1):
    imprimir_empleados()
    text = input('Nombre empleado: ')
    add_empleado(text)
    imprimir_empleados()
    
elif (text==2):
    imprimir_clientes()
    text = input('Nombre cliente: ')
    add_cliente(text)
    imprimir_clientes()
    
elif (text==3):
    text = input('Nombre producto: ')
    id = int(input('id empleado: '))
    add_venta(text, id)
    
elif (text==4):
    reporte_venta()

