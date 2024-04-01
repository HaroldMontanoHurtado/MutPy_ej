from db.connection import *

def add_empleado(nombre):
    with app.app_context():
        quary="""INSERT INTO empleados (nombre) VALUES(%s);"""
        try:
            cur = mysql.connection.cursor()
            cur.execute(quary, (nombre,))
            mysql.connection.commit()
            cur.close()
            print('ejecutó add_empleado()')
        except (Exception) as error:
            print(error)

def add_cliente(nombre):
    with app.app_context():
        quary= """INSERT INTO clientes (nombre) VALUES(%s);"""
        try:
            cur = mysql.connection.cursor()
            cur.execute(quary, (nombre,))
            mysql.connection.commit()
            cur.close()
            print('ejecutó add_cliente()')
        except (Exception) as error:
            print(error)

def add_venta(producto, id_empleado):
    with app.app_context():
        quary="""INSERT INTO ventas (producto, id_empleado) VALUES(%s, %s);"""
        try:
            cur = mysql.connection.cursor()
            cur.execute(quary, (producto, id_empleado,))
            mysql.connection.commit()
            cur.close()
            print('ejecutó add_venta()')
        except (Exception) as error:
            print(error)

def imprimir_empleados():
    with app.app_context():
        quary="SELECT * FROM empleados"
        try:
            cur = mysql.connection.cursor()
            cur.execute(quary)
            empleados = cur.fetchall()
            print("\nEmpleados:")
            for empleado in empleados:
                print(f"ID: {empleado[0]}, Nombre: {empleado[1]}")
        except Exception as ex:
            print(f"Error al obtener los empleados:\n{ex}")

def imprimir_clientes():
    with app.app_context():
        quary="SELECT * FROM clientes"
        try:
            cur = mysql.connection.cursor()
            cur.execute(quary)
            clientes = cur.fetchall()
            print("\nClientes:")
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
            cur = mysql.connection.cursor()
            cur.execute(quary)
            ventas = cur.fetchall()
            print("\nReporte de ventas:")
            for venta in ventas:
                print(f"Cant. Vendida: {venta[1]}, Empleado: {venta[0]}")
                #print(venta)
        except Exception as ex:
            print(f"Error al obtener las ventas:\n{ex}")

def prueba_consulta():
    print('Prueba consultas db')
