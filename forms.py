from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class LoginForm(FlaskForm):
    username = StringField('Логин')
    password = StringField('Пароль')
    submit = SubmitField('Войти')

class RegisterForm(FlaskForm):
    name = StringField('Имя')
    surname = StringField('Фамилия')
    birthday = StringField('Дата рождения')
    login = StringField('Логин')
    password = StringField('Пароль')
    submit = SubmitField('Зарегистрироваться')
