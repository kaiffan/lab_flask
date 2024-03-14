from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, Regexp
from flask_wtf import FlaskForm, RecaptchaField


class LoginForm(FlaskForm):
    username = StringField(
        'Username',
        validators=[DataRequired(), Length(min=2, max=16)]
    )
    password = PasswordField(
        'Password',
        validators=[
            DataRequired(),
            Length(min=8),
            Regexp(regex='^(?=^.{8,}$)((?=.*\d)|(?=.*\W+))(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$',
                   message='The password must be at least 8 characters, it is mandatory to share uppercase, ' +
                           'lowercase letters, numbers, symbols')
        ]
    )
    remember_me = BooleanField('Remember me', default=False, validators=[DataRequired()])
    recaptcha = RecaptchaField()
    submit = SubmitField('Sign in')


class RegistrationForm(FlaskForm):
    username = StringField(
        'Login',
        validators=[DataRequired(), Length(min=2, max=16)]
    )
    name = StringField(
        'First_name',
        validators=[
            DataRequired(),
            Length(min=4, max=16),
            Regexp(regex='^[a-яА-Я]+$')
        ]
    )
    surname = StringField(
        'Last_name',
        validators=[
            DataRequired(),
            Length(min=2, max=32),
            Regexp(regex='^([А-ЯЁ][а-яё]{2,15})(-[А-ЯЁ][а-яё]{2,15})?$',
                   message='Double surname in which each surname is ' +
                           'from 2 to 15 characters separated by a dash')
        ]
    )
    password = PasswordField(
        'Password',
        validators=[
            DataRequired(),
            Length(min=8),
            EqualTo('confirm_password', message='Passwords must match'),
            Regexp(regex='^(?=^.{8,}$)((?=.*\d)|(?=.*\W+))(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$',
                   message='The password must be at least 8 characters, it is mandatory to share uppercase, ' +
                           'lowercase letters, numbers, symbols')
        ]
    )
    confirm_password = PasswordField('Repeat password')
    accept_rules = BooleanField(
        'I accept the rules of the site',
        default=False,
        validators=[DataRequired()]
    )
    recaptcha = RecaptchaField()
    submit = SubmitField('Registration')
