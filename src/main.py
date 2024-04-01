from db.consultas import *
from test.test_crud import *

print(' - - - - CRUD - - - -')
print('1. Añadir empleados.')
print('2. Añadir cliente.')
print('3. Añadir ventas.')
print('4. Reporte de ventas.')

text = int(input('Digite: '))

if (text==1):
    
    text = input('Nombre empleado: ')
    add_empleado(text)
    
elif (text==2):
    text = input('Nombre cliente: ')
    add_cliente(text)
    
elif (text==3):
    text = input('Nombre producto: ')
    id = int(input('id empleado: '))
    add_venta(text, id)
    
elif (text==4):
    reporte_venta()

