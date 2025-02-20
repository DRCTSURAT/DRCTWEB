import os
from flask import Flask, render_template, request, flash, redirect, url_for
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "default-secret-key")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/mission')
def mission():
    return render_template('mission.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/donate', methods=['GET', 'POST'])
def donate():
    if request.method == 'POST':
        amount = request.form.get('amount')
        name = request.form.get('name')
        email = request.form.get('email')
        
        # Here you would typically integrate with a payment gateway
        flash('Thank you for your donation! We will contact you soon.', 'success')
        return redirect(url_for('donate'))
    
    return render_template('donate.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        # Here you would typically send an email or store the contact form data
        flash('Thank you for your message! We will get back to you soon.', 'success')
        return redirect(url_for('contact'))
    
    return render_template('contact.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
