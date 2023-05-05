from flask import Flask
from flask_mysqldb import MySQL


app = Flask(__name__)

app.secret_key = '1ec8fb36c578c721e00d4143c6d2c2f66bbffb4d7fdb58bcf36a6a8deac713bc'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'CHICHARITOBLUE4'
app.config['MYSQL_DB'] = 'farmaciasguadalajara'
mysql = MySQL(app)
