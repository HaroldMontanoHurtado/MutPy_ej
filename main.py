from db.consultas import *
from calls import *

print(' - - - - CRUD - - - -')
print('1. Añadir empleados.')
print('2. Añadir cliente.')
print('3. Añadir ventas.')
print('4. Reporte de ventas.')
print('5. Salir.')
print('6. Cant. de productos vendidos por empleado.')
print('7. Lista empleados.')
print('8. Lista clientes.')
print('9. Lista reporte de ventas.')

while(True):
    opc = int(input('\nDigite una de las opciones: '))

    if (opc==1):
        txt = input('Nombre empleado: ')
        add_empleado(txt)
        
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
    elif (opc==6):
        id = input('id empleado: ')
        cant = prod_vendidos(id)
        print(f' El empleado {id} a vendido {cant} productos')
    elif (opc==7):
        print(lis_emp())
    elif (opc==8):
        print(lis_clt())
    elif (opc==9):
        print(lis_report_vent())
    else:
        pass
