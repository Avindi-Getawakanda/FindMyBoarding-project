from flask import Flask, render_template, request, redirect, url_for, session, jsonify, flash
from conn import create_connection
from Authentication import register_owner, owner_login
from Add_listing import add_listing
from view_listing import view_listings
from rent_cal import rent_calculator
import os

app = Flask(__name__)
app.secret_key = 'your-secret-key-change-this-in-production'  # Change this to a random secret key

# Home page
@app.route('/')
def index():
    return render_template('index.html')

# Student dashboard
@app.route('/student')
def student_dashboard():
    return render_template('student_dashboard.html')

# Owner dashboard
@app.route('/owner')
def owner_dashboard():
    if 'owner_id' not in session:
        return redirect(url_for('owner_login_page'))
    return render_template('owner_dashboard.html')

# Owner registration page
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            register_owner(email, password)
            flash('Registration successful! Please login.', 'success')
            return redirect(url_for('owner_login_page'))
        except Exception as e:
            flash('Registration failed. Email might already exist.', 'error')
            return render_template('register.html')
    return render_template('register.html')

# Owner login page
@app.route('/login', methods=['GET', 'POST'])
def owner_login_page():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        owner = owner_login(email, password)
        if owner:
            session['owner_id'] = owner['id']
            session['owner_email'] = owner['email']
            flash('Login successful!', 'success')
            return redirect(url_for('owner_dashboard'))
        else:
            flash('Invalid credentials.', 'error')
    return render_template('login.html')

# Add listing page
@app.route('/add-listing', methods=['GET', 'POST'])
def add_listing_page():
    if 'owner_id' not in session:
        return redirect(url_for('owner_login_page'))
    
    if request.method == 'POST':
        try:
            owner_id = session['owner_id']
            title = request.form['title']
            image_path = request.form['image_path']
            address = request.form['address']
            distance = float(request.form['distance'])
            price = float(request.form['price'])
            facilities = request.form['facilities']
            contact = request.form['contact']
            description = request.form['description']
            
            # Validate contact number
            if len(contact) != 10 or not contact.isdigit():
                flash('Contact number must be exactly 10 digits.', 'error')
                return render_template('add_listing.html')
            
            add_listing(owner_id, title, image_path, address, distance, price, facilities, contact, description)
            flash('Listing added successfully!', 'success')
            return redirect(url_for('owner_dashboard'))
        except Exception as e:
            flash('Error adding listing. Please try again.', 'error')
    
    return render_template('add_listing.html')

# View listings API endpoint
@app.route('/api/listings')
def get_listings():
    try:
        connection = create_connection()
        cursor = connection.cursor(dictionary=True)
        query = "SELECT title, address, distance_from_campus, price, facilities, contact, description FROM listings"
        cursor.execute(query)
        results = cursor.fetchall()
        connection.close()
        return jsonify(results)
    except Exception as e:
        return jsonify({'error': 'Failed to fetch listings'}), 500

# My listings API endpoint (for owners)
@app.route('/api/my-listings')
def get_my_listings():
    if 'owner_id' not in session:
        return jsonify({'error': 'Not authenticated'}), 401
    
    try:
        connection = create_connection()
        cursor = connection.cursor(dictionary=True)
        query = "SELECT title, address, distance_from_campus, price, facilities, contact, description FROM listings WHERE owner_id = %s"
        cursor.execute(query, (session['owner_id'],))
        results = cursor.fetchall()
        connection.close()
        return jsonify(results)
    except Exception as e:
        return jsonify({'error': 'Failed to fetch listings'}), 500

# Rent calculator
@app.route('/rent-calculator', methods=['GET', 'POST'])
def rent_calculator_page():
    if request.method == 'POST':
        try:
            income = float(request.form['income'])
            expenses = float(request.form['expenses'])
            budget = rent_calculator(income, expenses)
            return render_template('rent_calculator.html', budget=budget, income=income, expenses=expenses)
        except Exception as e:
            flash('Please enter valid numbers.', 'error')
    
    return render_template('rent_calculator.html')

# Logout
@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.', 'info')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)