import os
from flask import Flask, render_template, request, flash, redirect, url_for
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)
# Use the secret key from environment variable without a default value for security
app.secret_key = os.environ.get("SESSION_SECRET")

@app.route('/')
def index():
    try:
        return render_template('index.html')
    except Exception as e:
        logger.error(f"Error rendering index page: {str(e)}")
        return render_template('404.html'), 500

@app.route('/about')
def about():
    try:
        return render_template('about.html')
    except Exception as e:
        logger.error(f"Error rendering about page: {str(e)}")
        return render_template('404.html'), 500

@app.route('/mission')
def mission():
    try:
        return render_template('mission.html')
    except Exception as e:
        logger.error(f"Error rendering mission page: {str(e)}")
        return render_template('404.html'), 500

@app.route('/services')
def services():
    try:
        return render_template('services.html')
    except Exception as e:
        logger.error(f"Error rendering services page: {str(e)}")
        return render_template('404.html'), 500

@app.route('/donate', methods=['GET', 'POST'])
def donate():
    try:
        if request.method == 'POST':
            amount = request.form.get('amount')
            name = request.form.get('name')
            email = request.form.get('email')

            # Here you would typically integrate with a payment gateway
            flash('Thank you for your donation! We will contact you soon.', 'success')
            return redirect(url_for('donate'))

        return render_template('donate.html')
    except Exception as e:
        logger.error(f"Error in donate page: {str(e)}")
        flash('An error occurred while processing your request.', 'error')
        return render_template('404.html'), 500

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    try:
        if request.method == 'POST':
            name = request.form.get('name')
            email = request.form.get('email')
            message = request.form.get('message')

            # Here you would typically send an email or store the contact form data
            flash('Thank you for your message! We will get back to you soon.', 'success')
            return redirect(url_for('contact'))

        return render_template('contact.html')
    except Exception as e:
        logger.error(f"Error in contact page: {str(e)}")
        flash('An error occurred while processing your request.', 'error')
        return render_template('404.html'), 500

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404