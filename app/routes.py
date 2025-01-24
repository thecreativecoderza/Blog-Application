from flask import render_template, redirect, url_for, request
from flask_login import login_user, logout_user, login_required, current_user
from app import app, db
from app.models import User, BlogPost
from app.forms import LoginForm, PostForm
from app.auth import check_password

@app.route('/')
@app.route('/home')
def home():
    posts = BlogPost.query.all()  # Retrieve all blog posts from the database
    return render_template('post_list.html', posts=posts)

@app.route('/post/<int:id>')
def post_detail(id):
    post = BlogPost.query.get_or_404(id)  # Retrieve a specific post by ID, or show a 404 page if not found
    return render_template('post_detail.html', post=post)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:  # Check if the user is already logged in
        return redirect(url_for('home'))  # Redirect to home if user is logged in
    
    form = LoginForm()  # Instantiate the login form
    if form.validate_on_submit():  # Check if the form is submitted and valid
        user = User.query.filter_by(username=form.username.data).first()  # Find the user by username
        if user and check_password(form.password.data, user.password_hash):  # Verify password
            login_user(user)  # Log the user in
            return redirect(url_for('home'))  # Redirect to home page after successful login
    return render_template('login.html', form=form)  # Render login page with form

@app.route('/logout')
def logout():
    logout_user()  # Log the user out
    return redirect(url_for('home'))  # Redirect to home after logout

@app.route('/create', methods=['GET', 'POST'])
@login_required
def create_post():
    form = PostForm()  # Instantiate the post creation form
    if form.validate_on_submit():  # Check if the form is submitted and valid
        post = BlogPost(title=form.title.data, content=form.content.data, author=current_user)  # Create new post
        db.session.add(post)  # Add the post to the session
        db.session.commit()  # Commit the session to save the post in the database
        return redirect(url_for('home'))  # Redirect to the homepage after creating the post
    return render_template('create_post.html', form=form)  # Render post creation page with form
