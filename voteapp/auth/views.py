import sys
from flask import Flask, Blueprint, request, render_template, redirect, url_for, flash, abort
from flask_login import login_user, login_required, logout_user
from voteapp import db
from voteapp.models import Member
from voteapp.auth.forms import LoginForm, RegistrationForm
from werkzeug.security import generate_password_hash, check_password_hash
from wtforms import ValidationError
from flask_login import login_user, login_required, logout_user, current_user

'''
============================================================
                        AUTH
============================================================
'''

auth_blueprint = Blueprint('auth',
                              __name__,
                              template_folder='templates/auth')

@auth_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out!')
    return redirect(url_for('auth.login'))

#TODO: for some reason this form is never valid.  We can trick it by
# using request.method.  It is true on submit for the login form, but
# not here.  This is because we are not passing the CSRF
# https://stackoverflow.com/questions/10722968/flask-wtf-validate-on-submit-is-never-executed
# TODO:  Strip surrounding spaces
@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print("LOGIN: Valid Form on Login Submit: ", form.validate_on_submit(), file=sys.stderr)
        next = request.args.get('next')
        print("1 POST NEXT: ", next, file=sys.stderr)
        # Grab the user from our User Models table
        name = form.name.data
        name = name.lower()
        member = Member.query.filter_by(name=name).first()
        print(type(member), file=sys.stderr)
        # Check that the user was supplied and the password is right
        # The verify_password method comes from the User object
        # https://stackoverflow.com/questions/2209755/python-operation-vs-is-not
        if member is not None:
            isValid = member.checkPassword(form.password.data)
            print("Password Match: ", isValid, file=sys.stderr)

            #If password matches, log in the user
            if (isValid):
                login_user(member)
                flash('Logged in successfully.')
                # If a user was trying to visit a page that requires a login
                # flask saves that URL as 'next'.  Check if that next exists,
                # otherwise we'll go to the welcome page. Next is not being captured
                #in the request.
                next = request.args.get('next')
                print("2 POST NEXT: ", next, file=sys.stderr)
                if next == None or not next[0]=='/':
                    next = url_for('vote.vote')
                return redirect(next)
            else: # bad password
                flash('Your password is incorrect.')
                return render_template('login.html', form=form)
        else: # Member not in the db
            flash('Login name not found, please register.')
            return render_template('login.html', form=form)

    print("LOGIN:  Valid Form on login GET: ", form.validate_on_submit(), file=sys.stderr)
    next = request.args.get('next')
    print("GET NEXT: ", next, file=sys.stderr)
    return render_template('login.html', form=form)

'''
This magically does email validation. When bad email is entered it will display
the form again, but it will not say what is wrong.  It preserves the values
entered previoulsly.

https://wtforms.readthedocs.io/en/stable/crash_course.html#displaying-errors
'''
# TODO:  Strip surrounding spaces
@auth_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        print("REGISTER:  Valid Form on Register Submit: ", form.validate_on_submit(), file=sys.stderr)
        name = form.name.data
        name = name.lower()
        print("REGISTER:  Valid Form on Register Submit: ", name, file=sys.stderr)
        password = form.password.data

        # Check to see if the email is already registered.
        # TODO: If this gets triggered what do with do with the message and the
        # error.  This is how we propagte a raised error. Don't forget the import.
        try:
            form.checkName(name)
            toAdd = Member(name, password)
            db.session.add(toAdd)
            db.session.commit()
            flash('Thanks for registering! Now you can login!')
            return redirect(url_for('auth.login'))
        except ValidationError as err:
            print("ValidationError: ", err.args, file=sys.stderr)
            flash('Email address already registered.')
            #flash(err.args)
            return render_template('register.html', form=form)

    print("REGISTER:  Valid Form on GET: ", form.validate_on_submit(), file=sys.stderr)
    return render_template('register.html', form=form)
