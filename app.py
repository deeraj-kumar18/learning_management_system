# app.py
from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import check_password_hash
import logging
from db import Database  # Import the Database class from db.py module

app = Flask(__name__)
app.secret_key = '9fce27c5bd0b2ba35607b8dafafed0021875a46ef656c7ea'

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize Database instance
db = Database()

# Route for login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = db.authenticate_user(username, password)
        if user:
            session['user_id'] = user[0]  # Store user ID in session
            flash(f'Welcome, {username}!', 'success')
            if user[3] == 'student':
                return redirect(url_for('student_dashboard'))
            elif user[3] == 'teacher':
                return redirect(url_for('teacher_dashboard'))
        else:
            flash('Invalid username or password', 'error')
            logger.warning(f'Invalid login attempt for username: {username}')
    return render_template('login.html')

# Route for logout
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('You have been logged out', 'info')
    return redirect(url_for('login'))

# Route for student dashboard
@app.route('/student/dashboard')
def student_dashboard():
    if 'user_id' in session:
        # Implementation of student dashboard (not provided)
        return render_template('student_dashboard.html')
    else:
        return redirect(url_for('login'))

# Route for teacher dashboard
@app.route('/teacher/dashboard')
def teacher_dashboard():
    if 'user_id' in session:
        # Implementation of teacher dashboard (not provided)
        return render_template('teacher_dashboard.html')
    else:
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
