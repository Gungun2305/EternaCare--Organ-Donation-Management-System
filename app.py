from flask import Flask, render_template, request, redirect, url_for, flash # Basic Flask imports
from flask_sqlalchemy import SQLAlchemy # It is used to interact with the database
from datetime import datetime # It is used to get the current date and time
from urllib.parse import quote # It encoded the password for safety
import secrets # It is used to generate a random secret key for flash messages
import os
from dotenv import load_dotenv
from urllib.parse import quote


app = Flask(__name__)  # Initialize the Flask app

# Load environment variables from .env file
load_dotenv()

# Get values from environment
password = quote(os.getenv('DB_PASSWORD'))
secret_key = os.getenv('SECRET_KEY', secrets.token_hex(16))  # fallback if not set

# Configure secret key and DB URI
app.config['SECRET_KEY'] = secret_key
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://root:{password}@localhost/organ_donation_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # It is used to avoid modification tracking

# Initialize the database
db = SQLAlchemy(app)

# Database Models
class Donor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    blood_type = db.Column(db.String(10), nullable=False)  
    organ_needed = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    message = db.Column(db.Text, nullable=True)
    registered_on = db.Column(db.DateTime, default=datetime.utcnow)
    
class Recipient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    blood_type = db.Column(db.String(10), nullable=False)  
    organ_needed = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    message = db.Column(db.Text, nullable=True)
    registered_on = db.Column(db.DateTime, default=datetime.utcnow)

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    message = db.Column(db.Text, nullable=False)
    contacted_on=db.Column(db.DateTime, default=datetime.utcnow)

# Routes
@app.route('/') 
def main():
    return render_template('first.html') 

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/donors', methods=['GET', 'POST'])
def donor_registration():
    if request.method == 'POST': # If the form is Submitted
        name = request.form.get('name')
        age = request.form.get('age')
        blood_type = request.form.get('blood_type')
        organ_needed = request.form.get('organ_needed')
        email = request.form.get('email')
        message = request.form.get('message')

        if not email:
            return "Email is required"

        new_donor = Donor(name=name, email=email, age=age,blood_type=blood_type,organ_needed=organ_needed, message=message)
        db.session.add(new_donor) # Add the data to the database
        db.session.commit()  # Save the data to the database
        
        flash("Registration successful! Thank you for becoming an organ donor.", "success") # Flash message

        return redirect(url_for('main'))
    return render_template('donors.html')

@app.route('/Recipients', methods=['GET', 'POST']) 
def recipient_registration():
    if request.method == 'POST': 
        name = request.form.get('name')
        age = request.form.get('age')
        blood_type = request.form.get('blood_type')
        organ_needed = request.form.get('organ_needed')
        email = request.form.get('email')
        message = request.form.get('message')

        print(request.form)  

        if not email:
            return "Email is required"

        new_recipient = Recipient(name=name, email=email,age=age,blood_type=blood_type, organ_needed=organ_needed, message=message)
        db.session.add(new_recipient)
        db.session.commit()

        flash("Registration successful! Thank you for becoming a Recipient.", "success")

        return redirect(url_for('main'))
    return render_template('Recipients.html')


@app.route('/Contact_Us', methods=['GET', 'POST'])
def contact_us():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')


        if not email:
            return "Email is required"

        new_contact = Contact(name=name, email=email, message=message) 
        db.session.add(new_contact) 
        db.session.commit() 

        flash("Thank you for reaching out! We will get back to you soon. ", "success")

        return redirect(url_for('main'))
    return render_template('Contact_Us.html')

# Main Function
if __name__ == '__main__':
    # Create database tables if they do not exist
    with app.app_context(): 
        db.create_all() 
    app.run(debug=True)
