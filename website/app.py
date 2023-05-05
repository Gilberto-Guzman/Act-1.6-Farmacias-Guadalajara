import io
import re
import csv
from flask import (
    Response,
    make_response,
    render_template,
    request,
    redirect,
    url_for,
    session
)
from mysqlconnection import *
import MySQLdb.cursors

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate, Table, TableStyle

from io import BytesIO


@ app.route("/")
def index():
    return render_template("views/home/home.html")


@ app.route("/home")
def home():
    return render_template("views/home/home.html")


@ app.route("/contact")
def contact():
    return render_template("views/contact/contact.html")


@ app.route("/login", methods=['GET', 'POST'])
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


@ app.route("/register", methods=['GET', 'POST'])
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


@ app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return redirect(url_for('home'))


@ app.route('/dashboard')
def dashboard():
    return render_template('views/dashboard/dashboard.html')


# ---CUENTAS---
@ app.route('/account')
def account():
    if session.get('loggedin') == True and session.get('username') == 'Administrador' and session.get('id') == -1:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts')
        accounts = cursor.fetchall()
        cursor.close()
        return render_template('views/account/account.html', accounts=accounts)

    else:
        return redirect('/home')


@ app.route('/searchaccount', methods=['GET', 'POST'])
def searchaccount():
    if session.get('loggedin') == True and session.get('username') == 'Administrador' and session.get('id') == -1:

        searchaccount = request.form['searchaccount']
        filtered_accounts = []

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts')
        accounts = cursor.fetchall()

        for account in accounts:
            if searchaccount in str(account['id']) or searchaccount in account['username'] or searchaccount in account['password'] or searchaccount in account['email']:
                filtered_accounts.append(account)

        return render_template('views/account/account.html', accounts=filtered_accounts)
    else:
        return redirect('/home')


@ app.route('/editaccount', methods=['GET', 'POST'])
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


@ app.route('/deleteaccount', methods=['GET', 'POST'])
def deleteaccount():
    if session.get('loggedin') == True and session.get('username') == 'Administrador' and session.get('id') == -1:
        user_id = request.form['user_id']
        cursor = mysql.connection.cursor()
        cursor.execute("DELETE FROM accounts WHERE id = %s", (user_id,))
        mysql.connection.commit()
        return redirect('/account')
    else:
        return redirect('/home')


@ app.route('/onclickeditaccount', methods=['GET', 'POST'])
def onclickeditaccount():
    if session.get('loggedin') == True and session.get('username') == 'Administrador' and session.get('id') == -1:
        session['user_id'] = request.form['user_id']
        session['editform'] = True

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("SELECT * FROM accounts WHERE id = %s",
                       (session['user_id'],))
        session['user_information'] = cursor.fetchone()
        return redirect('/account')
    else:
        return redirect('/home')


@ app.route('/onclickecreateaccount', methods=['GET', 'POST'])
def onclickecreateaccount():
    if session.get('loggedin') == True and session.get('username') == 'Administrador' and session.get('id') == -1:
        session['createform'] = True

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


@ app.route('/accountmysqltopdf')
def accountmysqltopdf():
    if session.get('loggedin') == True and session.get('username') == 'Administrador' and session.get('id') == -1:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts')
        data = cursor.fetchall()

        buffer = BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=letter)
        styles = getSampleStyleSheet()

        elements = []

        header_style = ParagraphStyle(
            name="header", alignment=TA_CENTER, fontSize=24)

        elements.append(
            Paragraph('Lista de cuentas<br/><br/><br/>', header_style))

        t = Table([['ID', 'Usuario', 'Correo Electronico']] + [[account['id'],
                  account['username'], account['email']] for account in data])
        t.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.red),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
            ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 14),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
            ('ALIGN', (0, 1), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 1), (-1, -1), 12),
            ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
        ]))
        elements.append(t)

        doc.build(elements)

        pdf_data = buffer.getvalue()

        response = make_response(pdf_data)
        response.headers['Content-Type'] = 'application/pdf'
        response.headers['Content-Disposition'] = 'attachment; filename=accounts.pdf'
        return response
    else:
        return redirect('/home')


# ---DOCTORES---
@ app.route('/doctor')
def doctor():
    if session.get('loggedin') == True and session.get('username') == 'Administrador' and session.get('id') == -1:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM doctors')
        doctors = cursor.fetchall()
        cursor.close()
        return render_template('views/doctor/doctor.html', doctors=doctors)
    else:
        return redirect('/home')


@ app.route('/searchdoctor', methods=['GET', 'POST'])
def searchdoctor():
    if session.get('loggedin') == True and session.get('username') == 'Administrador' and session.get('id') == -1:

        searchdoctor = request.form['searchdoctor']
        filtered_doctors = []

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM doctors')
        doctors = cursor.fetchall()

        for doctor in doctors:
            if searchdoctor in str(doctor['id']) or searchdoctor in doctor['fullname'] or searchdoctor in doctor['speciality'] or searchdoctor in doctor['address'] or searchdoctor in doctor['email'] or searchdoctor in doctor['phonenumber']:
                filtered_doctors.append(doctor)

        return render_template('views/doctor/doctor.html', doctors=filtered_doctors)
    else:
        return redirect('/home')


@ app.route('/editdoctor', methods=['GET', 'POST'])
def editdoctor():
    if session.get('loggedin') == True and session.get('username') == 'Administrador' and session.get('id') == -1:
        id = request.form['id']
        fullname = request.form['fullname']
        speciality = request.form['speciality']
        address = request.form['address']
        email = request.form['email']
        phonenumber = request.form['phonenumber']

        # cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor = mysql.connection.cursor()
        cursor.execute("UPDATE doctors SET id =%s, fullname=%s, speciality=%s, address=%s, email=%s, phonenumber=%s WHERE id=%s",
                       (id, fullname, speciality, address, email, phonenumber, session['user_id'],))
        mysql.connection.commit()
        session.pop('editform', None)
        return redirect('/doctor')
    else:
        return redirect('/home')


@ app.route('/createdoctor', methods=['GET', 'POST'])
def createdoctor():
    if session.get('loggedin') == True and session.get('username') == 'Administrador' and session.get('id') == -1:
        id = request.form['id']
        fullname = request.form['fullname']
        speciality = request.form['speciality']
        address = request.form['address']
        email = request.form['email']
        phonenumber = request.form['phonenumber']
        # cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor = mysql.connection.cursor()
        cursor.execute(
            'INSERT INTO doctors VALUES (%s, % s, % s, % s, % s, % s)', (id, fullname, speciality, address, email, phonenumber))
        mysql.connection.commit()
        session.pop('createform', None)
        return redirect('/doctor')
    else:
        return redirect('/home')


@ app.route('/deletedoctor', methods=['GET', 'POST'])
def deletedoctor():
    if session.get('loggedin') == True and session.get('username') == 'Administrador' and session.get('id') == -1:
        user_id = request.form['user_id']
        cursor = mysql.connection.cursor()
        cursor.execute("DELETE FROM doctors WHERE id = %s", (user_id,))
        mysql.connection.commit()
        return redirect('/doctor')
    else:
        return redirect('/home')


@ app.route('/onclickeditdoctor', methods=['GET', 'POST'])
def onclickeditdoctor():
    if session.get('loggedin') == True and session.get('username') == 'Administrador' and session.get('id') == -1:
        session['user_id'] = request.form['user_id']
        session['editform'] = True

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("SELECT * FROM doctors WHERE id = %s",
                       (session['user_id'],))
        session['user_information'] = cursor.fetchone()
        return redirect('/doctor')
    else:
        return redirect('/home')


@ app.route('/onclickedcreatedoctor', methods=['GET', 'POST'])
def onclickedcreatedoctor():
    if session.get('loggedin') == True and session.get('username') == 'Administrador' and session.get('id') == -1:
        session['createform'] = True

        return redirect('/doctor')
    else:
        return redirect('/home')


@ app.route('/doctormysqltocsv')
def doctormysqltocsv():
    if session.get('loggedin') == True and session.get('username') == 'Administrador' and session.get('id') == -1:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(
            'SELECT id, fullname, speciality, address, email, phonenumber FROM doctors')
        accounts = cursor.fetchall()
        csv_file = io.StringIO()
        writer = csv.writer(csv_file)
        writer.writerow(['ID', 'Nombre Completo', 'Especialidad',
                        'Direccion', 'Correo Electronico', 'Numero de Telefono'])
        for row in accounts:
            writer.writerow(
                [
                    row['id'],
                    row['fullname'],
                    row['speciality'],
                    row['address'],
                    row['email'],
                    row['phonenumber']
                ]
            )
        response = Response(csv_file.getvalue(), mimetype='text/csv')
        response.headers.set('Content-Disposition',
                             'attachment', filename='doctors.csv')
        return response
    else:
        return redirect('/home')


@ app.route('/doctormysqltopdf')
def doctormysqltopdf():
    if session.get('loggedin') == True and session.get('username') == 'Administrador' and session.get('id') == -1:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM doctors')
        data = cursor.fetchall()

        buffer = BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=letter)
        styles = getSampleStyleSheet()

        elements = []

        header_style = ParagraphStyle(
            name="header", alignment=TA_CENTER, fontSize=24)

        elements.append(
            Paragraph('Lista de doctores<br/><br/><br/>', header_style))

        t = Table(
            [[
                'ID',
                'Nombre Completo',
                'Especialidad',
                'Direccion',
                'Correo Electronico',
                'Numero de Telefono'
            ]] + [[
                doctor['id'],
                doctor['fullname'],
                doctor['speciality'],
                doctor['address'],
                doctor['email'],
                doctor['phonenumber']]
                for doctor in data])
        t.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.red),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
            ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 10),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
            ('ALIGN', (0, 1), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 1), (-1, -1), 9),
            ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
        ]))
        elements.append(t)

        doc.build(elements)

        pdf_data = buffer.getvalue()

        response = make_response(pdf_data)
        response.headers['Content-Type'] = 'application/pdf'
        response.headers['Content-Disposition'] = 'attachment; filename=doctors.pdf'
        return response
    else:
        return redirect('/home')


# ---PACIENTES---
@ app.route('/patient')
def patient():
    if session.get('loggedin') == True and session.get('username') == 'Administrador' and session.get('id') == -1:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM patients')
        patients = cursor.fetchall()
        cursor.close()
        return render_template('views/patient/patient.html', patients=patients)
    else:
        return redirect('/home')


@ app.route('/searchpatient', methods=['GET', 'POST'])
def searchpatient():
    if session.get('loggedin') == True and session.get('username') == 'Administrador' and session.get('id') == -1:

        searchpatient = request.form['searchpatient']
        filtered_patients = []

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM patients')
        patients = cursor.fetchall()

        for patient in patients:
            if searchpatient in str(patient['id']) or searchpatient in patient['fullname'] or searchpatient in patient['dateofbirth'] or searchpatient in patient['address'] or searchpatient in patient['phonenumber']:
                filtered_patients.append(patient)

        return render_template('views/patient/patient.html', patients=filtered_patients)
    else:
        return redirect('/home')


@ app.route('/editpatient', methods=['GET', 'POST'])
def editpatient():
    if session.get('loggedin') == True and session.get('username') == 'Administrador' and session.get('id') == -1:
        id = request.form['id']
        fullname = request.form['fullname']
        dateofbirth = request.form['dateofbirth']
        address = request.form['address']
        phonenumber = request.form['phonenumber']

        # cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor = mysql.connection.cursor()
        cursor.execute("UPDATE patients SET id =%s, fullname=%s, dateofbirth=%s, address=%s, phonenumber=%s WHERE id=%s",
                       (id, fullname, dateofbirth, address, phonenumber, session['user_id'],))
        mysql.connection.commit()
        session.pop('editform', None)
        return redirect('/patient')
    else:
        return redirect('/home')


@ app.route('/createpatient', methods=['GET', 'POST'])
def createpatient():
    if session.get('loggedin') == True and session.get('username') == 'Administrador' and session.get('id') == -1:
        id = request.form['id']
        fullname = request.form['fullname']
        dateofbirth = request.form['dateofbirth']
        address = request.form['address']
        phonenumber = request.form['phonenumber']
        # cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor = mysql.connection.cursor()
        cursor.execute(
            'INSERT INTO patients VALUES (%s, % s, % s, % s, % s)', (id, fullname, dateofbirth, address, phonenumber))
        mysql.connection.commit()
        session.pop('createform', None)
        return redirect('/patient')
    else:
        return redirect('/home')


@ app.route('/deletepatient', methods=['GET', 'POST'])
def deletepatient():
    if session.get('loggedin') == True and session.get('username') == 'Administrador' and session.get('id') == -1:
        user_id = request.form['user_id']
        cursor = mysql.connection.cursor()
        cursor.execute("DELETE FROM patients WHERE id = %s", (user_id,))
        mysql.connection.commit()
        return redirect('/patient')
    else:
        return redirect('/home')


@ app.route('/onclickeditpatient', methods=['GET', 'POST'])
def onclickeditpatient():
    if session.get('loggedin') == True and session.get('username') == 'Administrador' and session.get('id') == -1:
        session['user_id'] = request.form['user_id']
        session['editform'] = True

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("SELECT * FROM patients WHERE id = %s",
                       (session['user_id'],))
        session['user_information'] = cursor.fetchone()
        return redirect('/patient')
    else:
        return redirect('/home')


@ app.route('/onclickedcreatepatient', methods=['GET', 'POST'])
def onclickedcreatepatient():
    if session.get('loggedin') == True and session.get('username') == 'Administrador' and session.get('id') == -1:
        session['createform'] = True

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

        return redirect('/patient')
    else:
        return redirect('/home')


@ app.route('/patientmysqltocsv')
def patientmysqltocsv():
    if session.get('loggedin') == True and session.get('username') == 'Administrador' and session.get('id') == -1:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(
            'SELECT id, fullname, dateofbirth, address, phonenumber FROM patients')
        patients = cursor.fetchall()
        csv_file = io.StringIO()
        writer = csv.writer(csv_file)
        writer.writerow(['ID', 'Nombre Completo', 'Fecha de Nacimiento',
                        'Direccion', 'Numero de Telefono'])
        for row in patients:
            writer.writerow(
                [
                    row['id'],
                    row['fullname'],
                    row['dateofbirth'],
                    row['address'],
                    row['phonenumber']
                ]
            )
        response = Response(csv_file.getvalue(), mimetype='text/csv')
        response.headers.set('Content-Disposition',
                             'attachment', filename='patients.csv')
        return response
    else:
        return redirect('/home')


@ app.route('/patientmysqltopdf')
def patientmysqltopdf():
    if session.get('loggedin') == True and session.get('username') == 'Administrador' and session.get('id') == -1:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM patients')
        data = cursor.fetchall()

        buffer = BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=letter)
        styles = getSampleStyleSheet()

        elements = []

        header_style = ParagraphStyle(
            name="header", alignment=TA_CENTER, fontSize=24)

        elements.append(
            Paragraph('Lista de pacientes<br/><br/><br/>', header_style))

        t = Table(
            [[
                'ID',
                'Nombre Completo',
                'Fecha de Nacimiento',
                'Direccion',
                'Numero de Telefono'
            ]] + [[
                doctor['id'],
                doctor['fullname'],
                doctor['dateofbirth'],
                doctor['address'],
                doctor['phonenumber']]
                for doctor in data])
        t.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.red),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
            ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 10),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
            ('ALIGN', (0, 1), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 1), (-1, -1), 9),
            ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
        ]))
        elements.append(t)

        doc.build(elements)

        pdf_data = buffer.getvalue()

        response = make_response(pdf_data)
        response.headers['Content-Type'] = 'application/pdf'
        response.headers['Content-Disposition'] = 'attachment; filename=patients.pdf'
        return response
    else:
        return redirect('/home')

# --------------------------------------------


# --- Citas ---
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


@ app.route('/searchappointment', methods=['GET', 'POST'])
def searchappointment():
    if session.get('loggedin') == True and session.get('username') == 'Administrador' and session.get('id') == -1:

        searchappointment = request.form['searchappointment']
        filtered_appointments = []

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM appointments')
        appointments = cursor.fetchall()

        for appointment in appointments:
            if searchappointment in str(appointment['id']) or searchappointment in appointment['patientname'] or searchappointment in appointment['dateandtime'] or searchappointment in appointment['reasonofthevisit'] or searchappointment in appointment['fullnameandspecialitydoctor']:
                filtered_appointments.append(appointment)

        return render_template('views/appointment/appointment.html', appointments=filtered_appointments)
    else:
        return redirect('/home')


@ app.route('/editappointment', methods=['GET', 'POST'])
def editappointment():
    if session.get('loggedin') == True and session.get('username') == 'Administrador' and session.get('id') == -1:
        id = request.form['id']
        patientname = request.form['patientname']
        dateandtime = request.form['dateandtime']
        reasonofthevisit = request.form['reasonofthevisit']
        fullnameandspecialitydoctor = request.form['fullnameandspecialitydoctor']
        # cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor = mysql.connection.cursor()
        cursor.execute("UPDATE appointments SET id =%s, patientname=%s, dateandtime=%s, reasonofthevisit=%s, fullnameandspecialitydoctor=%s WHERE id=%s",
                       (id, patientname, dateandtime, reasonofthevisit, fullnameandspecialitydoctor, session['user_id'],))
        mysql.connection.commit()
        session.pop('editform', None)
        return redirect('/appointment')
    else:
        return redirect('/home')


@ app.route('/createappointment', methods=['GET', 'POST'])
def createappointment():
    if session.get('loggedin') == True and session.get('username') == 'Administrador' and session.get('id') == -1:
        id = request.form['id']
        patientname = request.form['patientname']
        dateandtime = request.form['dateandtime']
        reasonofthevisit = request.form['reasonofthevisit']
        fullnameandspecialitydoctor = request.form['fullnameandspecialitydoctor']
        # cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor = mysql.connection.cursor()
        cursor.execute(
            'INSERT INTO appointments VALUES (%s, % s, % s, % s, % s)', (id, patientname, dateandtime, reasonofthevisit, fullnameandspecialitydoctor))
        mysql.connection.commit()
        session.pop('createform', None)
        return redirect('/appointment')
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

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("SELECT * FROM appointments WHERE id = %s",
                       (session['user_id'],))
        session['user_information'] = cursor.fetchone()
        return redirect('/appointment')
    else:
        return redirect('/home')


@ app.route('/onclickecreatappointment', methods=['GET', 'POST'])
def onclickecreatappointment():
    if session.get('loggedin') == True and session.get('username') == 'Administrador' and session.get('id') == -1:
        session['createform'] = True

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(
            'SELECT `fullname`, `speciality` FROM `doctors`')
        session['doctor_information'] = cursor.fetchall()
        return redirect('/appointment')
    else:
        return redirect('/home')


@ app.route('/appointmentmysqltocsv')
def appointmentmysqltocsv():
    if session.get('loggedin') == True and session.get('username') == 'Administrador' and session.get('id') == -1:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(
            'SELECT id, patientname, dateandtime, reasonofthevisit, fullnameandspecialitydoctor FROM appointments')
        appointments = cursor.fetchall()
        csv_file = io.StringIO()
        writer = csv.writer(csv_file)
        writer.writerow(['ID', 'Paciente', 'Fecha y Hora',
                        'Razon de la Visita', 'Doctor Asignado'])
        for row in appointments:
            writer.writerow(
                [
                    row['id'],
                    row['patientname'],
                    row['dateandtime'],
                    row['reasonofthevisit'],
                    row['fullnameandspecialitydoctor']
                ]
            )
        response = Response(csv_file.getvalue(), mimetype='text/csv')
        response.headers.set('Content-Disposition',
                             'attachment', filename='appointments.csv')
        return response
    else:
        return redirect('/home')


@ app.route('/appointmentmysqltopdf')
def appointmentmysqltopdf():
    if session.get('loggedin') == True and session.get('username') == 'Administrador' and session.get('id') == -1:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM appointments')
        data = cursor.fetchall()

        buffer = BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=letter)
        styles = getSampleStyleSheet()

        elements = []

        header_style = ParagraphStyle(
            name="header", alignment=TA_CENTER, fontSize=24)

        elements.append(
            Paragraph('Lista de Citas<br/><br/><br/>', header_style))

        t = Table(
            [[
                'ID',
                'Paciente',
                'Fecha y Hora',
                'Razon de la Visita',
                'Doctor Asignado'
            ]] + [[
                doctor['id'],
                doctor['patientname'],
                doctor['dateandtime'],
                doctor['reasonofthevisit'],
                doctor['fullnameandspecialitydoctor']]
                for doctor in data])
        t.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.red),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
            ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 10),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
            ('ALIGN', (0, 1), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 1), (-1, -1), 9),
            ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
        ]))
        elements.append(t)

        doc.build(elements)

        pdf_data = buffer.getvalue()

        response = make_response(pdf_data)
        response.headers['Content-Type'] = 'application/pdf'
        response.headers['Content-Disposition'] = 'attachment; filename=appointments.pdf'
        return response
    else:
        return redirect('/home')


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


# if __name__ == '__main__':
#     app.run(host='0.0.0.0')
# if _name_ == '_main_':
#   app.run(debug=True, port=4000, host='0.0.0.0')
if __name__ == '__main__':
    app.run(debug=True)
