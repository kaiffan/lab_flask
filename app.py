from flask import Flask, render_template, flash, redirect
from forms import LoginForm, RegistrationForm
from flask_login import LoginManager
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
app.config['RECAPTCHA_PUBLIC_KEY'] = '6Ld74-oUAAAAAJC0UOY6PtrOrNcxQ2VQCfGAqBOC'
app.config['RECAPTCHA_PRIVATE_KEY'] = '6Ld74-oUAAAAAD2_Jl2IVKh2uCCI9OPX_7oTdLz4'


@app.route('/main_page')
def get_main_page():
    return render_template('main_page.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me = {}'.format(form.username.data, form.remember_me.data))
        return redirect('/main_page')
    return render_template('login_page.html', title='Sign in', form=form)


@app.route('/register', methods=['GET', 'POST'])
def registration():
    form = RegistrationForm()
    if form.validate_on_submit():
        return redirect('/main_page')
    return render_template('registration_page.html', title='Registration', form=form)


if __name__ == '__main__':
    app.run()
