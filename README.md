# MutPy_ej
Un ejemplo más complejo del uso de MutPy-Pynguin


# probar tests unitarios
python3 -m unittest -v test/test_crud.py

# Probar MutPy-Pynguin
mut.py --target consultas.py --unit-test test/test_crud.py -m


# ejecutar mutaciones
mut.py --target consultas.py --unit-test test/test_crud.py --report report.txt

--target consultas.py : especifica el archivo objetivo (en este caso, calculator.py).
--unit-test test/test_crud.py : especifica el archivo de pruebas unitarias (en este caso, test/test_crud.py).
-m : indica que deseas ver los resultados de la mutación.

# ejecutar mutaciones html
mut.py --target consultas.py --unit-test test/test_crud.py -m -c --report-html

# ejecutar mutaciones más agresivas y extensas
mut.py --target consultas.py --unit-test test/test_crud.py -m -c -e --report-html

# Error al intentar conectar al localhost con WSL
El error que estás experimentando indica que tu cliente no puede conectarse físicamente al servidor especificado1. Esto puede suceder si estás intentando conectarte a MySQL desde dentro de un entorno de WSL (Windows Subsystem for Linux) o un contenedor Docker.

Cuando intentas conectarte a 127.0.0.1 desde dentro de WSL o Docker, en realidad estás intentando conectarte al propio entorno de WSL o contenedor Docker, no a tu máquina host2. Como tu entorno de WSL o contenedor Docker no contiene tu base de datos, la conexión falla.

Desde dentro de un entorno de WSL o contenedor Docker, puedes llegar a la máquina host en la dirección IP 172.17.0.12. Por lo tanto, tu URI de base de datos debería ser SQLALCHEMY_DATABASE_URI=mysql://root:dbpass@172.17.0.1/powerdns.
