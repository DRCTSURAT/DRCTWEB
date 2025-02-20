import os
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET")

# Database configuration
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL", "sqlite:///site.db")
app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
    "pool_recycle": 300,
    "pool_pre_ping": True,
}

db = SQLAlchemy(app)

# Initialize Login Manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'admin_login'

@login_manager.user_loader
def load_user(user_id):
    return Admin.query.get(int(user_id))

# Import models after db initialization
from models import Admin, Content

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

# Admin routes
@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        admin = Admin.query.filter_by(username=username).first()

        if admin and admin.check_password(password):
            login_user(admin)
            flash('Login successful!', 'success')
            return redirect(url_for('admin_dashboard'))
        flash('Invalid username or password', 'error')

    return render_template('admin/login.html')

@app.route('/admin/dashboard')
@login_required
def admin_dashboard():
    content = Content.query.order_by(Content.last_updated.desc()).all()
    return render_template('admin/dashboard.html', content=content)

@app.route('/admin/content/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_content(id):
    content = Content.query.get_or_404(id)
    if request.method == 'POST':
        content.title = request.form.get('title')
        content.content = request.form.get('content')
        content.updated_by = current_user.id
        db.session.commit()
        flash('Content updated successfully!', 'success')
        return redirect(url_for('admin_dashboard'))

    return render_template('admin/edit_content.html', content=content)

@app.route('/admin/logout')
@login_required
def admin_logout():
    logout_user()
    flash('Logged out successfully', 'success')
    return redirect(url_for('admin_login'))