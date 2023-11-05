# Bell Labs Vote App

# Summary
- Voting app for use as a demo for Demo. Test.
- Azure elements built manually
- Git Hub Action created manually
- Keep this running until Udacity Nano Degree complete (as part of the Udacity Exercise)

## Status

[![Build and deploy Python app to Azure Web App - GranierPythonApp](https://github.com/programmingkitchen/bell-labs-vote/actions/workflows/main_granierpythonapp.yml/badge.svg)](https://github.com/programmingkitchen/bell-labs-vote/actions/workflows/main_granierpythonapp.yml)


# TODO (Infrastructure)
- Udacity Exercise that includes
  - 404 Page Not Found Rule
  - App Service Plan
  - App Service (Python)
  - LAW
  - Action Group for 404 Alerts
- Instrument the Bell Labs App using the Simple Logger in the Selenium Project and injesting into LAW (manual config). 
[Collecting logs](https://learn.microsoft.com/en-us/azure/azure-monitor/agents/data-collection-text-log?tabs=portal)

# Teardown
- This is configured in Git Hub Actions as the pipeline.
- Manually delete in Azure (Billing)
- (OPTIONAL).  Delete the action.  Will it rebuild?

## References

- Article on configuration of gunicorn and nginx
https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-18-04

# Major Revision Planned
https://openai.com/blog/introducing-chatgpt-and-whisper-apis

# TODO (Application)
1. After voting, the selected radio button stays selected. Make this clear?
   - If you navigate to a different page and come back it goes to the default.
   - If you refresh it stays on the previous choice.
   - Maybe direct to a page that has "Top Recommendations" and "Vote Distribution" and a button that says "Vote Again"
1. Add admin user to be able to clear the DB via the application. Add link from the login page.
   - This currently works for a regular user, not just admin. How do we provide authorization to admin only.
   - http://localhost:5000/admin/admin
   - Changed admin to be host/admin
   - Working on this. Added code, but need to look at reset page more.
   - Add admin menu in template.
1. Format of Registration Page.
1. Add a variables file so that setup_dabase does not have hard coded passwords. Then put the .gitignore on the variables file, not the
   setup DB file.
1. Work on user profile and password reset (separate program).
1. Deal with this in the URL. It should not have the double "vote"
   - Just change the path to

```
@admin_blueprint.route('/')
```

http://localhost:5000/vote/vote

## Revision History

| DATE    | CHANGE                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 11/05/23 | Configure for ADO Pipelines |

| 7/20/23 | Configure for A&TT presentation. |
| 7/6/22  | Configure for deploy in Azure App Service via Git Hub Actions. Remove docs folder and put it in the directory below because something was finding the wsgi and causing error. C:\Users\rgran\Dropbox\PYTHON-PROGRAMS\FLASK\BELL-LABS-VOTE-RESOURCES. Clean up rating code. The rating system which was eventually removed can be found here: ~/Dropbox/PYTHON-PROGRAMS/FLASK/VOTE-ARCHIVE/VOTE-FINAL-TEMPLATES/VOTE-FINAL |
| 6/3/22  | Set up new repo and test. Update requirments.txt for a minimal packages.                                                                                                                                                                                                                                                                                                                                                  |
| 6/2/22  | Add AT&T theme and text after making it into a template. Add accordian. Remove the rating system.                                                                                                                                                                                                                                                                                                                         |
| 2/20/22 | Registration works, but you have to navigate to it directly and it's not formatted. Add registration link Explore option to add registration at the bottom so it's a one page. Embed video.                                                                                                                                                                                                                               |
| 2/20/22 | Fixed: You can register when you are logged in. How can a registration system be added to the Login page when it would require to "extensions?"                                                                                                                                                                                                                                                                           |

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

- We are storing the virtual environments in a VENV directory and not naming them with dots.

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
- When trying to load these external libraries through a proxy, we might have issues. For example, we might not get the "checks" from Font Awesome.

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

## Accordion not working in Azure App Service but works locally

- Accordian does not expand or collapse
- Flash messages do not close
- The "Read More" does open
- Nothing in the logs
  https://getbootstrap.com/docs/4.1/components/collapse/

- Suspect outbout connectivity to Java Script

- We can see the logs for the app
- No user for ftp
  Monitoring > Log stream

**SOLUTION:** Change the url from http to https like below.

https://developer.mozilla.org/en-US/docs/Web/Security/Mixed_content?utm_source=mozilla&utm_medium=firefox-console-errors&utm_campaign=default

```
<script src="https://code.jquery.com/jquery-3.3.1.min.js" integrity="sha256-FgpCb/KJQlLNfOu91ta32o/NMZxltwRo8QtmkMRdAu8="
    crossorigin="anonymous"></script>
```

## Issue running gunicorn on Windows

https://stackoverflow.com/questions/62788628/modulenotfounderror-no-module-named-fcntl

- We changed back from "application" to "app" and it worked so this is probably because of
  the docs directory (see below).

- original wsgi.py

```
#!/usr/bin/python3
#from voteapp import app
from voteapp import application

if __name__ == '__main__':
    #app.run(debug=True, host="0.0.0.0", port=5000)
    application.run()
```

## Docs directory causing errors because it was being inspected

- After removing the docs diretory which was being inspected for files and failing due to errors, changed
  "application" back to "app."

```
Generating `gunicorn` command for 'wsgi:app'

Failed to find attribute 'app' in 'wsgi'.
```

## ORM Error

- Orm error

```
/tmp/8db7e2fbe7f632b/antenv/lib/python3.10/site-packages/sqlalchemy/orm/query.py:196: SyntaxWarning: "is not" with a literal. Did you mean "!="?
```
