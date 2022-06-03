from voteapp import db, login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin

# The user_loader decorator allows flask-login to load the current user
# and grab their id.
@login_manager.user_loader
def load_user(memberId):
    return Member.query.get(memberId)

class Member(db.Model, UserMixin):
    __tablename__ = 'members'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), unique=True, index=True)
    passwordHash = db.Column(db.String(128))

    def __init__(self, name, password):
        self.name = name
        self.passwordHash = generate_password_hash(password)

    def checkPassword(self, password):
        # https://stackoverflow.com/questions/23432478/flask-generate-password-hash-not-constant-output
        return check_password_hash(self.passwordHash, password)

    def genPassword(self, password):
        return generate_password_hash(password)

class Vote(db.Model):
    __tablename__ = 'votes'
    id = db.Column(db.Integer, primary_key = True)
    userName = db.Column(db.String(64))
    voteName = db.Column(db.String(64))
    memberId = db.Column(db.Integer, db.ForeignKey("members.id"))

    def __init__(self, userName, voteName, memberId):
        self.userName = userName
        self.voteName = voteName
        self.memberId = memberId
