from flask import Flask
from models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///eduhub.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

'''Flask-SQLAlchemy creates and manages the engine here
Read the SQLALCHEMY_DATABASE_URI from config, 
create Engine that uses URI,
Manage Session and connection'''
db.init_app(app)

# Only run this once to create the database and tables
with app.app_context():
    db.create_all()
