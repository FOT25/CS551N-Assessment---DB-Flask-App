import random
import string
import mysql.connector

# Connect to the database
db = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="Lazer271980",
  database="firstappdb"
)

# Generate 4000 dummy records
for i in range(4000):
  county = ''.join(random.choices(string.ascii_uppercase, k=10))
  total_population = random.randint(0, 6500)
  urban_population = random.randint(0, 6500)
  gdp_per_capita = random.randint(0, 6500)
  total_land_area = random.randint(0, 6500)
  water_per_capita = random.randint(0, 6500)
  agric_labour_force = random.randint(0, 6500)
  total_labour_force = random.randint(0, 6500)
  total_comm_energy = random.randint(0, 6500)
  country_id = random.randint(1, 195)
  
  # Insert the record into the table
  cursor = db.cursor()
  sql = "INSERT INTO per_capita (country, total_population, urban_population, gdp_per_capita, total_land_area, water_per_capita, agric_labour_force, total_labour_force, total_comm_energy, country_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
  val = (county, total_population, urban_population, gdp_per_capita, total_land_area, water_per_capita, agric_labour_force, total_labour_force, total_comm_energy, country_id)
  cursor.execute(sql, val)
  db.commit()

print("4000 records inserted.")



# @app.route("/")
# def index():
#     return render_template("index.html")


# @app.route("/login", methods=['GET', 'POST'])
# def login_page():
#     if request.method == 'POST':
#         details = request.form
#         firstname = details['fname']
#         lastname = details['lname']
#         cur = mysql.connection.cursor()
#         cur.execute(''' INSERT INTO tbl_users (firstname, lastname) VALUES (%s, %s) ''', (firstname, lastname))
#         lastId = cur.lastrowid
#         mysql.connection.commit()
#         cur.close()
#         return 'success: ' + str(lastId)
#     return render_template("login.html")


# @app.route("/register", methods=['GET', 'POST'])
# def register_page():

#     if request.method == 'POST':
#         details = request.form
#         fname = details['name']
#         email = details['email']
#         phone = details['phone']
#         password = details['password']
#         cur = mysql.connection.cursor()
#         cur.execute(''' INSERT INTO tbl_users (fullname, email, phone, ypassword) VALUES (%s, %s, %s, %s) ''', (fname, email, phone, password))
#         lastId = cur.lastrowid
#         mysql.connection.commit()
#         cur.close()
#         return 'success: ' + str(lastId)
#     return render_template("register.html")

# @app.route("/dashboard")
# def home_page():
#         Items = PerCapita.query.all()
        
#         return render_template("home.html", percapitas=Items)

# @app.route("/reset", methods=['GET', 'POST'])
# def reset_page():
#     if request.method == 'POST':
#         details = request.form
#         email = details['email']
#         cur = mysql.connection.cursor()
#         cur.execute(''' INSERT INTO MyUsers (firstname) VALUES (%s) ''', (email))
#         lastId = cur.lastrowid
#         mysql.connection.commit()
#         cur.close()
#         return 'success: ' + str(lastId)
#     return render_template("reset.html")

# @app.route("/country")
# def country_page():
#         Items = Country.query.all()
#         return render_template("country.html", countries=Items)


from wapp import db

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    price = db.Column(db.Float(), nullable=False)
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))

    def __init__(self, name, description, barcode, price):
        self.name = name
        self.description = description
        self.barcode = barcode
        self.price = price

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    password = db.Column(db.String(length=60), nullable=False)
    budget = db.Column(db.Integer(), nullable=False, default=1000)
    items = db.relationship('Item', backref='owned_user', lazy=True)

class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String(length=30), nullable=False, unique=True)
    country_code = db.Column(db.String(length=5), nullable=False, unique=True)
    country_id = db.relationship('PerCapita', backref='owned_capital', lazy=True)

class PerCapita(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String(length=120), nullable=False, unique=True)
    total_population = db.Column(db.Integer(), nullable=False, default=0)
    urban_population = db.Column(db.Integer(), nullable=False, default=0)
    gdp_per_capita = db.Column(db.Integer(), nullable=False, default=0)
    total_land_area = db.Column(db.Integer(), nullable=False, default=0)
    water_per_capita = db.Column(db.Integer(), nullable=False, default=0)
    agric_labour_force = db.Column(db.Integer(), nullable=False, default=0)
    total_labour_force = db.Column(db.Integer(), nullable=False, default=0)
    total_comm_energy = db.Column(db.Integer(), nullable=False, default=0)
    country_id = db.Column(db.Integer(), db.ForeignKey('country.id'))