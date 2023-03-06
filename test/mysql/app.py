from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'CHICHARITOBLUE4'
app.config['MYSQL_DB'] = 'farmaciasguadalajara'

mysql = MySQL(app)


@app.route('/')
def test_mysql():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM accounts')
    results = cur.fetchall()
    cur.close()
    return str(results)


if __name__ == '__main__':
    app.run(debug=True)
