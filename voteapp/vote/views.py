import sys
from flask import Flask, Blueprint, render_template, request, render_template, redirect, url_for, flash, abort
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, SubmitField
from flask_login import login_required, current_user
from voteapp import db
from voteapp.models import Vote
from voteapp.vote.forms import VoteForm


'''
============================================================
                        VOTE
============================================================
'''
'''
    Tried to grab the result list up front.  This does not work because
    this results in needing two threads.   We put the query inside the flow
    for POST and GET (2 times) to get around this.

    The fetchall() converts from the SQLAlchemy Resultset Proxy (we previously iterated
    using the proxy) to a normal list (or list of tuples).  Now we do normal Python/Jinja
    iteration in the template.

    Default values doesn't work after the first visit to the page.  But it does after 
    leaving the page and coming back. 

    https://itecnote.com/tecnote/python-setting-default-value-after-initialization-in-selectfield-flask-wtforms/

    Once an instance of the form is created, the data is bound. 
    Changing the default after that doesn't do anything. 
    The reason changing choices works is because it affects validation, 
    which doesn't run until validate is called.

'''

vote_blueprint = Blueprint('vote',
                              __name__,
                              template_folder='templates/vote', static_folder='static')

@vote_blueprint.route('/vote', methods=['GET', 'POST'])
@login_required
def vote():
    form = VoteForm()
    data = []
    label = []
    sql = '''select voteName, count(*) as total
    from votes
    group by voteName
    order by total desc'''

    if form.validate_on_submit():
        userName = current_user.name
        voteName = form.show.data
        memberId = current_user.id
        print("VOTE: ", voteName, file=sys.stderr)
        print("USER: ", userName, file=sys.stderr)
        print("ID: ", memberId, file=sys.stderr)
        try:
            toAdd = Vote(userName, voteName, memberId)
            db.session.add(toAdd)
            db.session.commit()
            flash('Thanks for Voting!')
            resultList = db.engine.execute(sql)
            rows = resultList.fetchall()
            for i in rows:
                label.append(str(i[0]))
                data.append(i[1])
            print("End of the post, before render.", file=sys.stderr)
            return render_template('combo.html', form = form, results = rows, label = label, data = data)
        except:
            flash('Voting Error.')
            return render_template('combo.html', form = form, results = rows, label = label, data = data)

    # Convert the Result Set Proxy into a normal Python list.  convert
    # the list of tuples to two separate lists since the labels property and
    # data expect corresponding lists.
    print("GET: ", file=sys.stderr)
    resultList = db.engine.execute(sql)
    print("RESULTLIST: ", type(resultList), file=sys.stderr)
    rows = resultList.fetchall()
    for i in rows:
        label.append(str(i[0]))
        data.append(i[1])
    return render_template('combo.html', form = form, results = rows, label = label, data = data)
