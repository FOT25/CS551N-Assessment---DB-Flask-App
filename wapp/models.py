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

try:
    db.create_all()
except Exception as e:
    print(f"Error creating tables: {str(e)}")
