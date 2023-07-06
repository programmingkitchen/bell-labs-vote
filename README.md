# Bell Labs Vote App


# Summary
- Voting app for use as a demo for Demo.

## Referances

- Article on configuration of gunicorn and nginx

https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-18-04

## TODO
1. Add admin user to be able to clear the DB via the application.
1. Add a variables file so that setup_dabase does not have hard coded passwords.  Then put the .gitignore on the varialbes file, not the 
   setup DB file. 
1. After voting, the selected radio button stays selected.  Make this clear? 
1. Work on user profile and password reset (separate program). 

## Revision History
| DATE        | CHANGE |
| ----------- | ----------- |
| 6/3/22      | Set up new repo and test. Update requirments.txt for a minimal packages. |
| 6/2/22      | Add AT&T theme and text after making it into a template. Add accordian. Remove the rating system. |
| 2/20/22     | Registration works, but you have to navigate to it directly and it's not formatted. Add registration link Explore option to add registration at the bottom so it's a one page. Embed video. |
| 2/20/22     | Fixed:  You can register when you are logged in. How can a registration system be added to the Login page when it would require to "extensions?" |



# Configuration 
**Python Version**
```
$ python --version
Python 3.10.7
(flask)

```

**Git & Git Hub**

```
git@github.com:programmingkitchen/bell-labs-vote.git
```
**Local PC directory**
```
/c/Users/rgran/Dropbox/PYTHON-PROGRAMS/FLASK/BELL-LABS-VOTE
```

**Virtual Environment**
```
~/VENV/flask
```

# Command Cheats

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
pip freeze > requirements.txt
pip install -r requirements.txt

pip install --upgrade pip &&\
		pip install -r requirements.txt
```

# Examples
- Startup 

```
rgran@HPPAVILION-1 MINGW64 ~/VENV/flask
$ cd ~/Dropbox/PYTHON-PROGRAMS/FLASK/BELL-LABS-VOTE

rgran@HPPAVILION-1 MINGW64 ~/Dropbox/PYTHON-PROGRAMS/FLASK/BELL-LABS-VOTE (main)
$ source /c/Users/rgran/VENV/flask/Scripts/activate
(flask)

$ which gunicorn
/c/Users/rgran/Dropbox/PYTHON-PROGRAMS/FLASK/BELL-LABS-VOTE/\Users\rgran\VENV\flask/Scripts/gunicorn
(flask)

```



# NOTES
- This vote app uses blueprints, but the registration and login system are combined in "auth"
- The README.md file appears to have the ability to load stylesheets and display checks. See links in the main app.
- When trying to load these external libraries through a proxy, we might have issues.  For example, we might not get the "checks" from Font Awesome. 

- Fontawesome
- Bootstrap


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

# Trouble

- Issue running gunicorn on Windows
https://stackoverflow.com/questions/62788628/modulenotfounderror-no-module-named-fcntl


- original wsgi.py
```
#!/usr/bin/python3
#from voteapp import app
from voteapp import application

if __name__ == '__main__':
    #app.run(debug=True, host="0.0.0.0", port=5000)
    application.run()
```