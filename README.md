# Bell Labs Vote App


## Summary
Voting app for use as a demo for Automation Boot Camp

## Local PC directory
```
/c/Users/rgran/Dropbox/PYTHON-PROGRAMS/FLASK/BELL-LABS-VOTE
```

## Virtual Environmet Setup (Local PC Version)
* We are storing the virtual environments in a VENV directory and not naming them with dots.

```
~/VENV<env-name>

python -m venv ~/VENV/flask
source ~/VENV/flask/Scripts/activate

deactivate

```
## PIP
```
pip install --upgrade pip &&\
		pip install -r requirements.txt
```

## Examples
```
rgran@HPPAVILION-1 MINGW64 ~/Dropbox/PYTHON-PROGRAMS/FLASK/BELL-LABS-VOTE (main)
$ source ~/VENV/flask/Scripts/activate
(flask)


```

## Git & Git Hub

```
git@github.com:programmingkitchen/bell-labs-vote.git
```

## NOTES
* This vote app uses blueprints, but the registration and login system are combined in "auth"

```
pip freeze > requirements.txt
pip install -r requirementx.txt
```

* The README.md file appears to have the ability to load stylesheets and display checks. See links in the main app.

## TODO
1. Add admin user to be able to clear the DB via the application.

2. When trying to load these external libraries through a proxy, we might have issues.  For example, we might not get the "checks" from Font Awesome. 

* Fontawesome
* Bootstrap

  
## Revision History

### 6/3/22
* Set up new repo and test.
* Update requirments.txt for a minimal packages.

### 6/2/22
* Add AT&T theme and text after making it into a template.  
* Add accordian.
* Remove the rating system.

### 2/20/22
Registration works, but you have to navigate to it directly and it's not formatted.
* Add registration link.  Explore option to add registration at the bottom so it's a one page.
* Embed video

### 2/20/22
* Fixed:  You can register when you are logged in.
* How can a registration system be added to the Login page when it would require to "extensions?"


## All Imports
```
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
```

