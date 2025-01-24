from app import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    # Define the user model for storing user data
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    posts = db.relationship('BlogPost', backref='author', lazy=True)  # Relationship with BlogPost

    def __repr__(self):
        return f'<User {self.username}>'

class BlogPost(db.Model):
    # Define the blog post model for storing blog content
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=db.func.now())  # Default to current time
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # Foreign key to User model

    def __repr__(self):
        return f'<BlogPost {self.title}>'
