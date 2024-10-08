from flask import Flask, render_template, send_from_directory,request,url_for,redirect,session,flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'sessionkeybedo'  # Required for session management

# Route for Home page with navigation and background image# Route for home page
@app.route('/')
def home():
    return render_template('home.html')

# # Route for Login page
# @app.route('/login')
# def login():
#     return render_template('login.html')

# Route for About page
@app.route('/about')
def about():
    return render_template('about.html')

# Route to serve patient information disclosure
# @app.route('/disclosure/patients')
# def patient_info():
#     return send_from_directory(directory='disclosures', filename='patients.txt')

# Route to serve ERP user login disclosure
# @app.route('/disclosure/erp_users')
# def erp_user_info():
#     return send_from_directory(directory='disclosures', filename='erp_users.txt')

# Route for the login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Authenticate user
        conn = sqlite3.connect('medical_erp.db')
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'")
        user = cursor.fetchone()
        conn.close()

        if user:
            # Store user session
            session['username'] = username
            return redirect(url_for('register_patient'))  # Redirect to patient registration if login is successful
        else:
            flash('Invalid Credentials, Please try again')
            return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/signout', methods=['GET', 'POST'])
def signout():
    session.pop('username', None)
    return redirect(url_for('home'))    
# Route for the patient registration page
@app.route('/register', methods=['GET', 'POST'])
def register_patient():
    if 'username' not in session:
        return redirect(url_for('login'))  # Redirect to login if not authenticated

    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        entry_date = request.form['entry_date']
        blood_class = request.form['blood_class']
        permanent_diseases = request.form['permanent_diseases']

        # Save patient data into the database
        conn = sqlite3.connect('medical_erp.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO patients (name,age,entry_date, blood_class, permanent_diseases)
            VALUES (?, ?, ?, ?, ?)
        ''', (name,age,entry_date, blood_class, permanent_diseases))
        conn.commit()
        conn.close()

        flash('Registration successful!')  # Display success message
        return redirect(url_for('register_patient'))  # Stay on the same page to add more patients
    return render_template('registration.html')

# Route to query patient info (vulnerable to SQL injection)
@app.route('/query', methods=['GET', 'POST'])
def query_patient():
    if 'username' not in session:
        return redirect(url_for('login'))  # Redirect to login if not authenticated
    patient_data = None
    if request.method == 'POST':
        search_param = request.form['search_param']

        # SQL injection vulnerability
        conn = sqlite3.connect('medical_erp.db')
        cursor = conn.cursor()
        query = f"SELECT * FROM patients WHERE id = '{search_param}' OR name LIKE '%{search_param}%' LIMIT 10"
        cursor.execute(query)  # Vulnerable to SQL injection
        patient_data = cursor.fetchall()
        conn.close()

    return render_template('query.html', patient_data=patient_data)


if __name__ == '__main__':
    app.run(host="0.0.0.0")
