'''
    This version requires that we do db.create_all() to set up the database
    before we do anything else.  The creation of the account is optional.
    How can we create the db dynamically using Flask-SQLAlchemy?

'''

# Import database info
from voteapp import db
from voteapp.models import Member, Vote

# Create the tables in the database
# (Usually won't do it this way!)
db.create_all()

defaultpw = 'cangetin'
defaultadminpw = 'C@nget1n_N0w'

users = ['randall','test100', 'test101']

adminMember = Member('admin', 'password-clear')
adminMember.passwordHash = adminMember.genPassword(defaultadminpw)
db.session.add(adminMember)
db.session.commit()

for user in users:
    member = Member(user, 'password-clear')
    member.passwordHash = member.genPassword(defaultpw)
    db.session.add(member)
    db.session.commit()

vote = Vote('admin', 'Hamilton', '1')
db.session.add(vote)
db.session.commit()

print ("Setup complete.")
