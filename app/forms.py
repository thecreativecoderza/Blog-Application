from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class LoginForm(FlaskForm):
    # Form for user login
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=120)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class PostForm(FlaskForm):
    # Form for creating a new blog post
    title = StringField('Title', validators=[DataRequired(), Length(min=5, max=120)])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Create Post')
