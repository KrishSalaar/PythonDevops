from flask import Flask, render_template, request, redirect, url_for, session, flash
import os
from functools import wraps
from app import app

# app = Flask(__name__)
app.secret_key = os.urandom(24)  # Generate a random secret key for sessions

# Demo credentials (in a real app, you'd use a database)
USERS = {
    "admin": "password123",
    "demo": "demo123"
}

# Login decorator


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user' not in session:
            flash('Please login to access this page', 'error')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# Routes


@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username in USERS and USERS[username] == password:
            session['user'] = username
            flash('Login successful!', 'success')
            return redirect(url_for('documentation'))
        else:
            flash('Invalid credentials. Please try again.', 'error')

    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('user', None)
    flash('You have been logged out', 'info')
    return redirect(url_for('login'))


@app.route('/documentation')
@login_required
def documentation():
    # Define the documentation steps
    steps = [
        {
            "id": 1,
            "title": "Project Setup",
            "content": "Initial project setup including repository creation and configuration."
        },
        {
            "id": 2,
            "title": "AWS Account Creation",
            "content": "Setting up AWS to use appropriate services like EC2, EKS"
        },
        {
            "id": 3,
            "title": "Jenkins Configuration",
            "content": "Setting up Jenkins pipeline with appropriate plugins and configurations."
        },
        {
            "id": 4,
            "title": "AWS EKS Setup",
            "content": "Configuring AWS EKS cluster for Kubernetes deployment."
        },
        {
            "id": 5,
            "title": "Containerization",
            "content": "Creating Docker containers for the Python application."
        },
        {
            "id": 6,
            "title": "Kubernetes Deployment",
            "content": "Making Application.yaml file to deploy application to Kubernetes"
        },
        {
            "id": 7,
            "title": "CI/CD Pipeline",
            "content": "Setting up the continuous integration and deployment pipeline."
        },
        {
            "id": 8,
            "title": "Live Application",
            "content": "After Successful deployment check whether application is accessible with a URL"
        },
    ]

    return render_template('documentation.html', steps=steps, username=session['user'])


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
