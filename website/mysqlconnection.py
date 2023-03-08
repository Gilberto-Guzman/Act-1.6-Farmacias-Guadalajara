from flask import Flask, Blueprint, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

app = Flask(__name__)

app.secret_key = 'your secret key'

app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_USER'] = 'Gilberto'
app.config['MYSQL_PASSWORD'] = 'CHICHARITOBLUE4'
app.config['MYSQL_DB'] = 'farmaciasguadalajara'

mysql = MySQL(app)
