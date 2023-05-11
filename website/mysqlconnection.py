from flask import Flask
from flask_mysqldb import MySQL


app = Flask(__name__)

app.secret_key = '1ec8fb36c578c721e00d4143c6d2c2f66bbffb4d7fdb58bcf36a6a8deac713bc'

# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = 'CHICHARITOBLUE4'
# app.config['MYSQL_DB'] = 'farmaciasguadalajara'

app.config['MYSQL_HOST'] = 'db-mysql-nyc1-73231-do-user-14016281-0.b.db.ondigitalocean.com'
app.config['MYSQL_USER'] = 'doadmin'
app.config['MYSQL_PASSWORD'] = 'AVNS_4pFIZDPxXNQmGZE1Axx'
app.config['MYSQL_DB'] = 'farmaciasguadalajara'
app.config['MYSQL_PORT'] = 25060
app.config['MYSQL_SSL_MODE'] = 'REQUIRED'

mysql = MySQL(app)
