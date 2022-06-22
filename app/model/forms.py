import email
from unicodedata import name
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, PasswordField, BooleanField, EmailField, DateField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, Length, InputRequired


class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    remember_me = BooleanField('remember_me')


class SignUpForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    email = EmailField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[
        DataRequired(),
        Length(min=6, max=16)
    ])
    photo = FileField('image', validators=[
        FileAllowed(['jpg', 'png'], 'Images only!')
    ])

class MissingPersonForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    birthday = DateField('birthday', validators=[DataRequired()])
    birthplace = StringField('birthplace', validators=[DataRequired()])
    place_of_disappearance  = StringField('birthplace', validators=[DataRequired()])
    disappearance_details = TextAreaField('disappearance_details', validators=[DataRequired()])
    photo = FileField('image', validators=[
        FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!'),
        FileRequired()
    ])

class EditUserForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    email = EmailField('email', validators=[DataRequired(), Email()])
    photo = FileField('image', validators=[
        FileAllowed(['jpg', 'png'], 'Images only!')
    ])

class EditUserPassword(FlaskForm):
    current_password = PasswordField('old_password', validators=[DataRequired()])
    new_password = PasswordField('password', validators=[
        Length(min=6, max=16),
        InputRequired(),
        EqualTo('new_password', message='Passwords must match'),
    ])
    repeat_password = PasswordField(
        'repeat_password',
    )

class EditMissingPerson(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    birthday = DateField('birthday', validators=[DataRequired()])
    birthplace = StringField('birthplace', validators=[DataRequired()])
    place_of_disappearance  = StringField('birthplace', validators=[DataRequired()])
    disappearance_details = TextAreaField('disappearance_details', validators=[DataRequired()])
    photo = FileField('image', validators=[
        FileAllowed(['jpg', 'png'], 'Images only!')
    ])
