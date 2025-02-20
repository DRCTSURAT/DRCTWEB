from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class Admin(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256))
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# Add Content models
class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    page = db.Column(db.String(64), nullable=False)
    section = db.Column(db.String(64), nullable=False)
    title = db.Column(db.String(256))
    content = db.Column(db.Text)
    last_updated = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())
    updated_by = db.Column(db.Integer, db.ForeignKey('admin.id'))
