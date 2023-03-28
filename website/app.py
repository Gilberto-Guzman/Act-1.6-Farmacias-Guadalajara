import io
from flask import Response, render_template, request, redirect, url_for, session
from mysqlconnection import *
import MySQLdb.cursors
import re
import csv


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
            return redirect('/home')
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
    return redirect(url_for('home'))


@app.route('/dashboard')
def dashboard():
    return render_template('views/dashboard/dashboard.html')


# ---CUENTAS---
@app.route('/account')
def account():
    if session.get('loggedin') == True and session.get('username') == 'Administrador' and session.get('id') == -1:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts')
        accounts = cursor.fetchall()
        cursor.close()
        return render_template('views/account/account.html', accounts=accounts)
    else:
        return redirect('/home')


@app.route('/deleteaccount', methods=['GET', 'POST'])
def deleteaccount():
    if session.get('loggedin') == True and session.get('username') == 'Administrador' and session.get('id') == -1:
        user_id = request.form['user_id']
        cursor = mysql.connection.cursor()
        cursor.execute("DELETE FROM accounts WHERE id = %s", (user_id,))
        mysql.connection.commit()
        return redirect('/account')
    else:
        return redirect('/home')


@app.route('/onclickeditaccount', methods=['GET', 'POST'])
def onclickeditaccount():
    if session.get('loggedin') == True and session.get('username') == 'Administrador' and session.get('id') == -1:
        session['user_id'] = request.form['user_id']
        session['editform'] = True
        return redirect('/account')
    else:
        return redirect('/home')


@app.route('/onclickecreateaccount', methods=['GET', 'POST'])
def onclickecreateaccount():
    if session.get('loggedin') == True and session.get('username') == 'Administrador' and session.get('id') == -1:
        session['createform'] = True
        return redirect('/account')
    else:
        return redirect('/home')


@app.route('/editaccount', methods=['GET', 'POST'])
def editaccount():
    if session.get('loggedin') == True and session.get('username') == 'Administrador' and session.get('id') == -1:
        id = request.form['id']
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        # cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor = mysql.connection.cursor()
        cursor.execute("UPDATE accounts SET id =%s, username=%s, password=%s, email=%s WHERE id=%s",
                       (id, username, password, email, session['user_id'],))
        mysql.connection.commit()
        session.pop('editform', None)
        return redirect('/account')
    else:
        return redirect('/home')


@ app.route('/createaccount', methods=['GET', 'POST'])
def createaccount():
    if session.get('loggedin') == True and session.get('username') == 'Administrador' and session.get('id') == -1:
        id = request.form['id']
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        # cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor = mysql.connection.cursor()
        cursor.execute(
            'INSERT INTO accounts VALUES (%s, % s, % s, % s)', (id, username, password, email, ))
        mysql.connection.commit()
        session.pop('createform', None)
        return redirect('/account')
    else:
        return redirect('/home')


@ app.route('/accountmysqltocsv')
def accountmysqltocsv():
    if session.get('loggedin') == True and session.get('username') == 'Administrador' and session.get('id') == -1:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT id, username, password, email FROM accounts')
        accounts = cursor.fetchall()
        csv_file = io.StringIO()
        writer = csv.writer(csv_file)
        writer.writerow(['ID', 'Usuario', 'Contrasena', 'Correo Electronico'])
        for row in accounts:
            writer.writerow([row['id'], row['username'],
                            row['password'], row['email']])
        response = Response(csv_file.getvalue(), mimetype='text/csv')
        response.headers.set('Content-Disposition',
                             'attachment', filename='accounts.csv')
        return response
    else:
        return redirect('/home')


# --- Citas ---
@ app.route('/schedule', methods=['GET', 'POST'])
def schedule():
    msg = ''
    if session.get('loggedin') == True:
        if request.method == 'POST' and 'name' in request.form and 'address' in request.form and 'phonenumber' in request.form and 'reasonofthevisit' in request.form and 'dateandtime' in request.form:

            username = session['username']
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute(
                'SELECT email FROM accounts WHERE username = % s', (username, ))
            email = cursor.fetchone()['email']
            name = request.form['name']
            address = request.form['address']
            phonenumber = request.form['phonenumber']
            reasonofthevisit = request.form['reasonofthevisit']
            dateandtime = request.form['dateandtime']

            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute(
                'INSERT INTO appointments VALUES (NULL, % s, % s, % s, % s, % s, % s, % s)', (username, email, name, address, phonenumber, reasonofthevisit, dateandtime, ))
            mysql.connection.commit()
            msg = '¡Se ha registrado su cita correctamente!'
        return render_template('views/schedule/schedule.html', msg=msg)
    else:
        return redirect('/home')


@ app.route('/appointment')
def appointment():
    if session.get('loggedin') == True and session.get('username') == 'Administrador' and session.get('id') == -1:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM appointments')
        appointments = cursor.fetchall()
        cursor.close()
        return render_template('views/appointment/appointment.html', appointments=appointments)
    else:
        return redirect('/home')


@ app.route('/deleteappointment', methods=['GET', 'POST'])
def deleteappointment():
    if session.get('loggedin') == True and session.get('username') == 'Administrador' and session.get('id') == -1:
        user_id = request.form['user_id']
        cursor = mysql.connection.cursor()
        cursor.execute("DELETE FROM appointments WHERE id = %s", (user_id,))
        mysql.connection.commit()
        return redirect('/appointment')
    else:
        return redirect('/home')


@ app.route('/onclickeditappointment', methods=['GET', 'POST'])
def onclickeditappointment():
    if session.get('loggedin') == True and session.get('username') == 'Administrador' and session.get('id') == -1:
        session['user_id'] = request.form['user_id']
        session['editform'] = True
        return redirect('/appointment')
    else:
        return redirect('/home')


@ app.route('/onclickecreateappointment', methods=['GET', 'POST'])
def onclickecreateappointment():
    if session.get('loggedin') == True and session.get('username') == 'Administrador' and session.get('id') == -1:
        session['createform'] = True
        return redirect('/appointment')
    else:
        return redirect('/home')


@ app.route('/editappointment', methods=['GET', 'POST'])
def editappointment():
    if session.get('loggedin') == True and session.get('username') == 'Administrador' and session.get('id') == -1:
        id = request.form['id']
        username = request.form['username']
        email = request.form['email']
        name = request.form['name']
        address = request.form['address']
        phonenumber = request.form['phonenumber']
        reasonofthevisit = request.form['reasonofthevisit']
        dateandtime = request.form['dateandtime']
        # cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor = mysql.connection.cursor()
        cursor.execute("UPDATE appointments SET id =%s, username=%s, email=%s, name=%s, address=%s, phonenumber=%s, reasonofthevisit=%s, dateandtime=%s WHERE id=%s",
                       (id, username, email, name, address, phonenumber, reasonofthevisit, dateandtime, session['user_id'],))
        mysql.connection.commit()
        session.pop('editform', None)
        return redirect('/appointment')
    else:
        return redirect('/home')


@ app.route('/createappointment', methods=['GET', 'POST'])
def createappointment():
    if session.get('loggedin') == True and session.get('username') == 'Administrador' and session.get('id') == -1:
        id = request.form['id']
        username = request.form['username']
        email = request.form['email']
        name = request.form['name']
        address = request.form['address']
        phonenumber = request.form['phonenumber']
        reasonofthevisit = request.form['reasonofthevisit']
        dateandtime = request.form['dateandtime']
        # cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor = mysql.connection.cursor()
        cursor.execute(
            'INSERT INTO appointments VALUES (%s, % s, % s, % s, %s, % s, % s, % s)', (id, username, email, name, address, phonenumber, reasonofthevisit, dateandtime))
        mysql.connection.commit()
        session.pop('createform', None)
        return redirect('/appointment')
    else:
        return redirect('/home')


@ app.route('/appointmentmysqltocsv')
def appointmentmysqltocsv():
    if session.get('loggedin') == True and session.get('username') == 'Administrador' and session.get('id') == -1:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(
            'SELECT id, username, email, name, address, phonenumber, reasonofthevisit, dateandtime FROM appointments')
        accounts = cursor.fetchall()
        csv_file = io.StringIO()
        writer = csv.writer(csv_file)
        writer.writerow(['ID', 'Usuario', 'Correo Electronico', 'Nombre Completo',
                        'Direccion', 'Numero Telefonico', 'Motivo de La visita', 'Fecha y Hora'])
        for row in accounts:
            writer.writerow([row['id'], row['username'], row['email'], row['name'],
                            row['address'], row['phonenumber'], row['reasonofthevisit'], row['dateandtime']])

        response = Response(csv_file.getvalue(), mimetype='text/csv')
        response.headers.set('Content-Disposition',
                             'attachment', filename='appointments.csv')
        return response
    else:
        return redirect('/home')


# if __name__ == '__main__':
#     app.run(host='0.0.0.0')

# if _name_ == '_main_':
#   app.run(debug=True, port=4000, host='0.0.0.0')

if __name__ == '__main__':
    app.run(debug=True)
