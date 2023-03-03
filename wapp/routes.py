from wapp import app
from flask import render_template, request, url_for
from wapp.models import Item, Country, PerCapita
from flask_mysqldb import MySQL

mysql = MySQL(app)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        try:
            details = request.form
            firstname = details['fname']
            lastname = details['lname']
            cur = mysql.connection.cursor()
            cur.execute(''' INSERT INTO tbl_users (firstname, lastname) VALUES (%s, %s) ''', (firstname, lastname))
            lastId = cur.lastrowid
            mysql.connection.commit()
            cur.close()
            return 'success: ' + str(lastId)
        except Exception as e:
            return "An error occurred: " + str(e)
    return render_template("login.html")


@app.route("/register", methods=['GET', 'POST'])
def register_page():
    if request.method == 'POST':
        try:
            details = request.form
            fname = details['name']
            email = details['email']
            phone = details['phone']
            password = details['password']
            cur = mysql.connection.cursor()
            cur.execute(''' INSERT INTO tbl_users (fullname, email, phone, ypassword) VALUES (%s, %s, %s, %s) ''', (fname, email, phone, password))
            lastId = cur.lastrowid
            mysql.connection.commit()
            cur.close()
            return 'success: ' + str(lastId)
        except Exception as e:
            return "An error occurred: " + str(e)
    return render_template("register.html")

@app.route("/dashboard")
def home_page():
    try:
        Items = PerCapita.query.all()
        return render_template("home.html", percapitas=Items)
    except Exception as e:
        return "An error occurred: " + str(e)

@app.route("/reset", methods=['GET', 'POST'])
def reset_page():
    if request.method == 'POST':
        try:
            details = request.form
            email = details['email']
            cur = mysql.connection.cursor()
            cur.execute(''' INSERT INTO MyUsers (firstname) VALUES (%s) ''', (email))
            lastId = cur.lastrowid
            mysql.connection.commit()
            cur.close()
            return 'success: ' + str(lastId)
        except Exception as e:
            return "An error occurred: " + str(e)
    return render_template("reset.html")

@app.route("/country")
def country_page():
    try:
        Items = Country.query.all()
        return render_template("country.html", countries=Items)
    except Exception as e:
        return "An error occurred: " + str(e)
