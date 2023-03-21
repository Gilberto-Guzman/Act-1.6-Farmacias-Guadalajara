from flask import render_template, request, redirect, url_for, session
from mysqlconnection import *
import MySQLdb.cursors
import re


@app.route("/")
def index():
    return render_template("views/home/home.html")


@app.route("/home")
def home():
    return render_template("views/home/home.html")


@app.route("/contact")
def contact():
    return render_template("views/contact/contact.html")


@app.route("/login", methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(
            'SELECT * FROM accounts WHERE username = % s AND password = % s', (username, password, ))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            msg = '¡Ha iniciado sesión correctamente!'

            return render_template('views/home/home.html', msg=msg)
        else:
            msg = 'Usuario o contraseña incorrectos...'
    return render_template('views/login/login.html', msg=msg)


@app.route("/register", methods=['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(
            'SELECT * FROM accounts WHERE username = % s', (username, ))
        account = cursor.fetchone()
        if account:
            msg = 'Esta cuenta ya esta en uso...'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Correo electronico invalido...'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'El nombre de usuario debe contener solo caracteres y numeros...'
        elif not username or not password or not email:
            msg = '¡Porfavor rellene el formulario!'
        else:
            cursor.execute(
                'INSERT INTO accounts VALUES (NULL, % s, % s, % s)', (username, password, email, ))
            mysql.connection.commit()
            msg = '¡Se ha registrado correctamente!'
    elif request.method == 'POST':
        msg = '¡Porfavor rellene el formulario!'
    return render_template('views/register/register.html', msg=msg)


@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return redirect(url_for('login'))


@app.route('/dashboard')
def dashboard():
    return render_template('views/dashboard/dashboard.html')


@app.route('/appointment')
def appointment():
    if session.get('loggedin') == True:
        return render_template('views/appointment/appointment.html')
    else:
        msg = '¡Para solicitar una cita necesitamos que inicies sesión!'
        return render_template('views/login/login.html', msg=msg)

# if __name__ == '__main__':
#    app.run(host='0.0.0.0')


if __name__ == '__main__':
    app.run(debug=True)
