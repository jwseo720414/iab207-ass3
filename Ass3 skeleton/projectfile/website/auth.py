from flask import ( 
    Blueprint, flash, render_template, request, url_for, redirect
) 
from werkzeug.security import generate_password_hash,check_password_hash
from .models import User
from .forms import LoginForm,RegisterForm
from flask_login import login_user, login_required,logout_user
from .functions import check_upload_file

from . import db


#create a blueprint
bp = Blueprint('auth', __name__)


# this is the hint for a login function
@bp.route('/login', methods=['GET', 'POST'])
def authenticate():  # view function
    '''
    Login view function
    '''
    print('In Login View function')
    login_form = LoginForm()
    error = None
    if (login_form.validate_on_submit() == True):
        user_name = login_form.user_name.data
        password = login_form.password.data
        u1 = User.query.filter_by(username=user_name).first()
        if u1 is None:
            error = 'Incorrect user name'
        elif not check_password_hash(u1.password, password):  # takes the hash and password
            error = 'Incorrect password'
        if error is None:
            login_user(u1)
            nextp = request.args.get('next')  # this gives the url from where the login page was accessed
            if nextp is None or not nextp.startswith('/'):
                return redirect(url_for('main.index'))
            return redirect(nextp)
        else:
            flash(error)

    return render_template('user.html', form=login_form, title='Login')


@bp.route('/register', methods=['GET', 'POST'])
def register():
    '''
    Register a new user
    '''
    print('In Register View function')
    register_form = RegisterForm()
    error = None
    if (register_form.validate_on_submit() == True):
        username = register_form.user_name.data
        password = register_form.password.data
        email = register_form.email_id.data
        dob = register_form.dob.data

        # Check if user or email already taken
        u1 = User.query.filter_by(username=username).first()
        if u1 is not None:
            error = 'User \'${0}\' already exists'.format(username)

        u1 = User.query.filter_by(email=email).first()
        if u1 is not None:
            error = 'Email \'${0}\' already exists'.format(email)

        if error is None:
            u1 = User(
                username=username, password=generate_password_hash(password),
                email=email, dob=dob)
            db.session.add(u1)
            db.session.commit()
            return redirect(url_for('auth.authenticate'))
        else:
            flash(error)

    return render_template('user.html', form=register_form, title='Register')

@bp.route('/logout', methods=['GET'])
@login_required
def logout():
    '''
    Logout User
    '''
    logout_user()
    return redirect(url_for('main.index'))