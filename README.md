# Vote App 04


## Summary
Voting app for use as a demo.

## Notes
This vote app uses blueprints, but the registration and login system are combined in "auth"


## TODO
Add admin user to be able to clear the DB via the application.


## Revision History

### 6/4/22
* Set up new repo and test.

### 6/3/22
* Add AT&T theme and text after making it into a template.  
* Add accordian.
* Remove the rating system.

###2/20/22
Registration works, but you have to navigate to it directly and it's not formatted.
* Add registration link.  Explore option to add registration at the bottom so it's a one page.


## Issues

How to embed Video:  this works
<iframe width="560" height="315" src="https://www.youtube.com/embed/y881t8ilMyc" frameborder="0" allowfullscreen></iframe>

Supported mime type error with this:
<video width="320" height="240" controls>
 <source src="movie.mp4" type="video/mp4">
 <source src="movie.ogg" type="video/ogg">
Your browser does not support the video tag.
</video>

###2/20/22
* Fixed:  You can register when you are logged in.
* How can a registration system be added to the Login page when it would require to "extensions?"


## All Imports
import sys, os
from flask import Flask, render_template, request, render_template, redirect, url_for, flash, abort
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError




## Replacement Form with Styling

<!-- END Block Content -->

  <!-- Replacement Form This worked when put directly in the code.
  This doest not have any form styling.
  <form action="{{url_for('auth.login')}}" method = 'POST'>
      {# This hidden_tag is a CSRF security feature. #}
      {{ form.hidden_tag() }}
      {{ form.name.label }} {{ form.name() }}<br>
      {{ form.password.label }} {{ form.password() }}<br>
      {{ form.submit() }}
  </form>
-->

  <!-- Old form info.  This has all the styling fore the form.
  <form>
    <div class="form-group">
      <input type="text" class="form-control form-control-lg" placeholder="Username">
    </div>
    <div class="form-group">
      <input type="password" class="form-control form-control-lg" placeholder="Password">
    </div>
    <input type="submit" value="Login" class="btn btn-outline-light btn-block">
  </form>
-->

alias vrun='cd ~/Dropbox/PYTHON-PROGRAMS/FLASK/VOTE/; pwd; python app.py'


## REQUIREMENTS

NOTE:  These are currently installed, but not all may be necessary

alembic==1.2.1
aniso8601==8.0.0
bleach==3.1.0
certifi==2019.9.11
chardet==3.0.4
Click==7.0
Flask==1.1.1
Flask-HTTPAuth==3.3.0
Flask-Login==0.4.1
Flask-Migrate==2.5.2
Flask-RESTful==0.3.7
Flask-SQLAlchemy==2.4.1
Flask-WTF==0.14.2
httplib2==0.14.0
idna==2.8
itsdangerous==1.1.0
Jinja2==2.10.3
Mako==1.1.0
MarkupSafe==1.1.1
oauth2client==4.1.3
packaging==19.2
passlib==1.7.1
psycopg2-binary==2.8.4
pyasn1==0.4.7
pyasn1-modules==0.2.7
pyparsing==2.4.2
python-dateutil==2.8.0
python-editor==1.0.4
pytz==2019.3
redis==3.3.11
requests==2.22.0
rsa==4.0
six==1.12.0
SQLAlchemy==1.3.10
urllib3==1.25.6
virtualenv==16.7.8
webencodings==0.5.1
Werkzeug==0.16.0
WTForms==2.2.1

## TO DO
Implement safe_url
https://flask-login.readthedocs.io/en/latest/
if not is_safe_url(next):
            return flask.abort(400)


This app uses a login/registration system but does not use Flask Blueprint.
It is designed to be an ideal format for simple apps (not so big where
  blueprints are essential).

It uses:

WTforms
SQLalchemy
sqlite

The views are still part of app.py.  Separating them into their own file may
require blueprints.


## Git & Git Hub

Note:  all changes made at the command line are immediately reflected in
the Atom window.  

1.  Create Repo locally and commit.
2. Create Repo on Git Hub.
3. Attempt to "Publish on GitHub", but get error related to branch.  There is
"no branch" displayed in the window. On the command line, we see the master branch.

Alternate method.

0. Verify config.

  git config --list

1. Perform functions at first on the command line (see below).
2. Commit to the master branch results in the master appearing in the Atom window.
3. Add remote

git remote add origin https://github.com/rgranier/vote.git

4. Now we see the "Publish Icon" in the window.   Click the publish icon and
   it pushed without further auth necessary.


…or create a new repository on the command line
echo "# vote" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/rgranier/vote.git
git push -u origin master


…or push an existing repository from the command line
git remote add origin https://github.com/rgranier/vote.git
git push -u origin master
