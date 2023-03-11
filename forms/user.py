from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, TextAreaField, SubmitField, EmailField, IntegerField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password_again = PasswordField('Повторите пароль', validators=[DataRequired()])
    surname = StringField('Фамилия пользователя', validators=[DataRequired()])
    name = StringField('Имя пользователя', validators=[DataRequired()])
    age = IntegerField('Возраст пользователя', validators=[DataRequired()])
    pos = StringField('Положение пользователя', validators=[DataRequired()])
    spec = StringField('Специальность пользователя', validators=[DataRequired()])
    address = StringField('Адрес пользователя', validators=[DataRequired()])
    submit = SubmitField('Войти')