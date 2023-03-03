from flask import Flask, render_template, request, url_for
from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy
# from flaskext.mysql import MySQL
# from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Lazer271980@127.0.0.1/firstappdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
# db = SQLAlchemy(app)
# mysql database connection configuration
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Lazer271980'
app.config['MYSQL_DB'] = 'firstappdb'

mysql = MySQL(app)

from wapp import routes