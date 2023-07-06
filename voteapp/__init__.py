import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
#from flask_migrate import Migrate


# Create a login manager object
login_manager = LoginManager()
app = Flask(__name__)
app.url_map.strict_slashes = False

# Often people will also separate these into a separate config.py file
app.config['SECRET_KEY'] = 'mysecretkey'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'votes.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
#Migrate(app,db)

# We can now pass in our app to the login manager
login_manager.init_app(app)

# Tell users what view to go to when they need to login.
login_manager.login_view = "auth.login"

''''
NOTE! These imports need to come after you've defined db, otherwise you will
get errors in your models.py files.
NOTE:  1.  Import the blueprints defined in the Views
'''
from voteapp.main.views import main_blueprint
from voteapp.auth.views import auth_blueprint
from voteapp.vote.views import vote_blueprint
from voteapp.stats.views import stats_blueprint
from voteapp.admin.views import admin_blueprint



'''
NOTE:  2. Register the blueprints.  This prefix sets the link that is produced.
If the templates have the same name, then the first one registered will be
the one that is found.
https://stackoverflow.com/questions/7974771/flask-blueprint-template-folder
'''
application.register_blueprint(main_blueprint,url_prefix="/")
application.register_blueprint(auth_blueprint,url_prefix="/auth")
application.register_blueprint(vote_blueprint,url_prefix="/vote")
application.register_blueprint(stats_blueprint,url_prefix="/stats")
application.register_blueprint(admin_blueprint,url_prefix="/admin")
