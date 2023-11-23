from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import login_required, LoginManager, current_user, login_user
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
login_manager = LoginManager()

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(128))
    username = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(50))

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)



def create_app():
    # Create Flask app
    app = Flask(__name__)

    # Configure the app
    app.config['SECRET_KEY'] = 'your-secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    app.config['SQLALCHEMY_ECHO'] = True

    # Initialize database
    db.init_app(app)

    # Initialize login manager
    login_manager.init_app(app)

    # Create database tables (optional)
    with app.app_context():
        db.create_all()

    return app

app = create_app()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@app.route('/login', methods=['GET', 'POST'], endpoint='login')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('profile'))

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()

        if user and user.check_password(password):
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page or url_for('profile'))
        else:
            flash('Invalid username or password', 'error')

    return render_template('login.html')

@app.route('/signup', endpoint='signup', methods=['GET', 'POST'])
def signup():
    """Signup code here"""

    
    if request.method == "POST":
        name = request.form.get('name')
        password = request.form.get('password')
        username = request.form.get('username')

        user = User(name=name, username=username)
        user.set_password(password)
        print(user)
        db.session.add(user)
        db.session.commit()
        redirect(url_for('login'))


    return render_template('signup.html')

@app.route('/', endpoint='profile')
@login_required
def profile():
    """profile code here"""
    if not current_user.is_authenticated:
        return redirect('/login')
    return render_template('profile.html')


if __name__ == "__main__":
    app.run('0.0.0.0', 5555, debug=True)
