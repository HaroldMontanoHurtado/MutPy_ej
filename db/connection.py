from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = '172.18.0.1' #'127.0.0.1' #'localhost' # en windows # '172.18.0.1' # En Debian
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password' # normalmente es sin contraseña
app.config['MYSQL_DB'] = 'ejmutpy'

mysql = MySQL(app)

class conectarBD:
    def __init__(self):
        with app.app_context():
            try:
                self.connection = mysql.connection
                self.cursor = self.connection.cursor()
                print('Conexion exitosa a BD!!')
            except Exception as ex:
                print('ERROR al conectar la BD:\n', f'\t{ex}.')


    def cerrar(self):
        self.connection.commit()
        self.connection.close()
