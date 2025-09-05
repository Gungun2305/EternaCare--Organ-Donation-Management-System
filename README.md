<h1> 🩺Organ Donation Management System </h1>

A Flask-based web application for managing organ donors, recipients, and contact requests.
The project helps people register as donors or recipients, and includes a contact form for queries.

<h1>🚀 Features</h1>

  -Register as an organ donor with details like name, age, blood type, organ, and email.

  -Register as a recipient in need of an organ.

  -Submit a contact form for general queries.

  -All data stored securely in a MySQL database.

  -Uses environment variables (.env) for database password & secret key.

  -Provides flash messages for user-friendly alerts.

<h1>🛠️ Tech Stack</h1>

  -Backend: Flask(Python)

  -Database: MySQL with SQLAlchemy ORM

  -Frontend: HTML (Jinja2 Templates)

  -Environment Management: python-dotenv

  -Security: URL-encoded DB password & secret key

<h1>📂 Project Structure</h1>

<pre>
organ-donation-app/
│── app.py                  # Main Flask application
│── templates/              # HTML templates
│   ├── first.html
│   ├── about.html
│   ├── donors.html
│   ├── Recipients.html
│   └── Contact_Us.html
│── static/                 # CSS, JS, Images
│── .env                    # Environment variables (not committed to GitHub)
│── requirements.txt        # Dependencies
│── README.md               # Documentation
</pre>

<h1>⚙️ Setup & Installation</h1>

<h2>1️⃣ Clone the Repository</h2>

    git clone https://github.com/your-username/organ-donation-app.git
    cd organ-donation-app
<h2>2️⃣ Create a Virtual Environment</h2>

    python -m venv venv
    venv\Scripts\activate     # On Windows
    source venv/bin/activate  # On Mac/Linux
<h2>3️⃣ Install Dependencies</h2>

    pip install -r requirements.txt
<h2>4️⃣ Configure Environment Variables</h2>
    Create a .env file in the project root:
    
    DB_PASSWORD=your_mysql_password
    SECRET_KEY=your_secret_key
<h2>5️⃣ Set Up MySQL Database</h2>
    Login to MySQL and create the database:

    CREATE DATABASE organ_donation_db;
<h2>6️⃣ Run the Application</h2>

    python app.py

The app will be running at:
👉 http://127.0.0.1:5000/

<h1>🗄️ Database Models</h1>

  -Donor: Stores donor details (name, age, blood type, organ, email, message).

  -Recipient: Stores recipient details (name, age, blood type, organ, email, message).

  -Contact: Stores messages submitted via the contact form.

<h1>📸 Screens & Routes</h1>

  / → Home Page

  /about → About Page

  /donors → Donor Registration

  /Recipients → Recipient Registration

  /Contact_Us → Contact Form

<h1>🔒 Security Notes</h1>

  -Passwords and secret keys are stored in .env (never push this file to GitHub).

  -Database password is URL-encoded before use.

  -Flask secret key is auto-generated if not set in .env.
<br>
<br>
✨ Built with ❤️ by Gungun Pal












  
