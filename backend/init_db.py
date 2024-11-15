# init_db.py
from models import db
from flask import Flask
from sqlalchemy import text

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./travelmate.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Initialize the database
with app.app_context():
    db.create_all()
    print("Database tables created.")

    # Query the users table
    users = db.session.execute(text("SELECT * FROM users")).fetchall()
    print("Users:", users)

    # Query the trips table
    trips = db.session.execute(text("SELECT * FROM trips")).fetchall()
    print("Trips:", trips)