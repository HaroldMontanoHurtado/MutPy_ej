from consultas import *
from test.test_crud import *

print(' - - - - CRUD - - - -')
print('1. Añadir empleados.')
print('2. Añadir cliente.')
print('3. Añadir ventas.')
print('4. Reporte de ventas.')
print('5. Salir.')

while(True):
    opc = int(input('\nDigite una de las opciones: '))

    if (opc==1):
        imprimir_empleados()
        txt = input('Nombre empleado: ')
        id = add_empleado(txt)
        print(f'Empleado_id: {id}')
        imprimir_empleados()
        
    elif (opc==2):
        imprimir_clientes()
        txt = input('Nombre cliente: ')
        add_cliente(txt)
        imprimir_clientes()
        
    elif (opc==3):
        txt = input('Nombre producto: ')
        id = int(input('id empleado: '))
        add_venta(txt, id)
        
    elif (opc==4):
        reporte_venta()
        
    elif (opc==5):
        break
    else:
        pass
