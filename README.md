# Bell Labs Vote App


## Summary
Voting app for use as a demo for Automation Boot Camp

## Notes
This vote app uses blueprints, but the registration and login system are combined in "auth"

pip freeze > requirements.txt
pip install -r requirementx.txt

## TODO
Add admin user to be able to clear the DB via the application.

Issues with talking out over the proxy to.  We dont' get the checks.

<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.0.13/css/all.css" integrity="sha384-DNOHZ68U8hZfKXOrtjWvjxusGo9WQnrNx2sqG0tfsghAvtVlRW3tvkXWZh58N9jp"
  crossorigin="anonymous">
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css" integrity="sha384-WskhaSGFgHYWDcbwN70/dfYBj47jz9qbsMId/iRN3ewGhXQFZCSftd1LZCfmhktB"
  crossorigin="anonymous">
<link rel="stylesheet" href="/static/css/style.css">

  <i class="fas fa-check fa-2x"></i>
  
## Revision History

### 6/3/22
* Set up new repo and test.
* Update requirments.txt for a minimal packages.

### 6/2/22
* Add AT&T theme and text after making it into a template.  
* Add accordian.
* Remove the rating system.

###2/20/22
Registration works, but you have to navigate to it directly and it's not formatted.
* Add registration link.  Explore option to add registration at the bottom so it's a one page.
* Embed video

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
