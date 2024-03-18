from flask_login import logout_user, login_user, LoginManager, UserMixin
from flask import render_template, flash, redirect, Flask
from werkzeug.security import generate_password_hash, check_password_hash
from forms import LoginForm, RegistrationForm
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
login = LoginManager(app=app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1111@localhost:5433/flask_app'
db = SQLAlchemy(app=app)

app.config.from_object(Config)


@app.route('/main_page')
def get_main_page():
    return render_template('main_page.html')


@app.route('/login', methods=['GET', 'POST'])
def login_to_site():
    form = LoginForm()
    if form.validate_on_submit():
        user: User = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect('/login')
        login_user(user=user, remember=form.remember_me.data)
        return redirect('/main_page')
    return render_template('login_page.html', title='Sign in', form=form)


@app.route('/register', methods=['GET', 'POST'])
def registration_to_site():
    form = RegistrationForm()
    if form.validate_on_submit():
        reg_user = User()
        reg_user.username = form.username.data
        reg_user.set_password(form.password.data)
        db.session.add(reg_user)
        db.session.commit()
        return redirect('/main_page')
    return render_template('registration_page.html', title='Registration', form=form)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.route('/logout')
def logout():
    logout_user()
    return redirect('main_page.html')


if __name__ == '__main__':
    app.run()


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def set_password(self, password: str):
        self.password_hash = generate_password_hash(
            password=password
        )

    def check_password(self, password: str) -> bool:
        return check_password_hash(
            pwhash=self.password_hash,
            password=password
        )

    def repr(self):
        return '<User {}>'.format(self.username)