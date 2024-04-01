from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
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
