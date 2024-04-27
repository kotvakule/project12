from flask_wtf import *
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField, IntegerField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Логин')
    password = PasswordField('Пароль')
    submit = SubmitField('Войти')

class RegisterForm(FlaskForm):
    username = StringField('Логин*')
    name = StringField('Имя')
    surname = StringField('Фамилия*')
    birthday = DateField('Дата рождения')
    phone = StringField('Номер телефона*')
    password = PasswordField('Пароль*')
    submit = SubmitField('Register')
