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
