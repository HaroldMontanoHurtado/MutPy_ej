from .connection import *

def add_empleado(nombre):
    with app.app_context():
        quary="""INSERT INTO empleados (nombre) VALUES(%s);"""
        try:
            cursor = mysql.connection.cursor()
            cursor.execute(quary, (nombre,))
            mysql.connection.commit()
            print('ejecutó add_empleado()')
        except (Exception) as error:
            print(error)

def add_cliente(nombre):
    with app.app_context():
        quary= """INSERT INTO clientes (nombre) VALUES(%s);"""
        try:
            cursor = mysql.connection.cursor()
            cursor.execute(quary, (nombre,))
            mysql.connection.commit()
            print('ejecutó add_cliente()')
        except (Exception) as error:
            print(error)

def add_venta(producto, id_empleado):
    with app.app_context():
        quary="""INSERT INTO ventas (producto, id_empleado) VALUES(%s, %s);"""
        try:
            cursor = mysql.connection.cursor()
            cursor.execute(quary, (producto, id_empleado,))
            mysql.connection.commit()
            print('ejecutó add_venta()')
        except (Exception) as error:
            print(error)

def imprimir_clientes():
    with app.app_context():
        quary="SELECT * FROM empleados"
        try:
            cursor = mysql.connection.cursor()
            cursor.execute(quary)
            empleados = cursor.fetchall()
            print("Empleados:")
            for empleado in empleados:
                print(f"ID: {empleado[0]}, Nombre: {empleado[1]}")
        except Exception as ex:
            print(f"Error al obtener los empleados:\n{ex}")

def imprimir_clientes():
    with app.app_context():
        quary="SELECT * FROM clientes"
        try:
            cursor = mysql.connection.cursor()
            cursor.execute(quary)
            clientes = cursor.fetchall()
            print("Clientes:")
            for cliente in clientes:
                print(f"ID: {cliente[0]}, Nombre: {cliente[1]}")
        except Exception as ex:
            print(f"Error al obtener los clientes:\n{ex}")

def reporte_venta():
    with app.app_context():
        quary="""
SELECT E.nombre, COUNT(V.id) as ventas
FROM empleados E
JOIN ventas V ON E.id = V.id_empleado
GROUP BY E.nombre
ORDER BY ventas DESC;"""
        try:
            cursor = mysql.connection.cursor()
            cursor.execute(quary)
            ventas = cursor.fetchall()
            print("Reporte de ventas:")
            for venta in ventas:
                print(f"Cant. Vendida: {venta[1]}, Empleado: {venta[0]}")
                #print(venta)
        except Exception as ex:
            print(f"Error al obtener las ventas:\n{ex}")

def prueba_consultas():
    print('si consulta')
