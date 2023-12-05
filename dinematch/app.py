from datetime import datetime
from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import login_required, LoginManager, current_user, login_user, logout_user
from flask_sqlalchemy import SQLAlchemy
from models import User, db
import os

login_manager = LoginManager()

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
            flash('Logged in successfully.', 'success')
            return redirect(next_page or url_for('profile'))
        else:
            flash('Invalid username or password', 'error')

    return render_template('login.html')

@app.route('/signup', endpoint='signup', methods=['GET', 'POST'])
def signup():
    """Implement signup code here"""

    if request.method == "POST":
        username = request.form.get('username')
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        password = request.form.get('password')
        email = request.form.get('email')
        date_of_birth_str = request.form.get('date_of_birth')
        date_of_birth = datetime.strptime(date_of_birth_str, '%Y-%m-%d').date()
        bio = request.form.get('bio')
        location = request.form.get('location')
        gender = request.form.get('gender')
        phone_number = request.form.get('phone_number')


    #Check if user exists
        user = User.query.filter_by(username=username).first()
        if user:
            flash('Username already exists', 'error')
            return redirect(url_for('signup'))

        user = User(first_name=first_name, last_name=last_name, username=username, email=email, date_of_birth=date_of_birth, bio=bio, location=location, gender=gender, phone_number=phone_number)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        redirect(url_for('login'))


    return render_template('signup.html')

@app.route('/logout', endpoint='logout')
@login_required
def logout():
    """Implement logout code here"""
    if current_user.is_authenticated:
        logout_user()
        flash('Logged out successfully.', 'success')
    return redirect(url_for('login'))

@app.route('/', endpoint='profile')
@login_required
def profile():
    """profile code here"""
    if not current_user.is_authenticated:
        return redirect(url_for('login', next='/profile'))

    all_users = User.query.all()
    matched_users = []

    for user in all_users:
        if user.id != current_user.id:
            if user.hobby == current_user.hobby and user.gender != current_user.gender:
                matched_users.append(user)

    return render_template('profile.html', user=current_user, matched_users=matched_users)

@app.route('/edit-profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    if request.method == 'POST':
        current_user.first_name = request.form.get('first_name')
        current_user.last_name = request.form.get('last_name')
        current_user.email = request.form.get('email')
        current_user.location = request.form.get('location')
        current_user.bio = request.form.get('bio')
        current_user.gender = request.form.get('gender')
        current_user.hobby = request.form.get('hobby')

        # if 'profile_picture' in request.files:
        #     profile_picture = request.files['profile_picture']
        #     if profile_picture.filename != '':
        #         profile_picture.save(os.path.join(app.config['UPLOAD_FOLDER'], profile_picture.filename))
        #         current_user.profile_picture = profile_picture.filename

        db.session.commit()
        flash('Profile edited successfully.', 'success')
        return redirect('/profile')

    return render_template('edit-profile.html', user=current_user)

if __name__ == "__main__":
    app.run('0.0.0.0', 5555, debug=True)
