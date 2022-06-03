import sys
from flask import Flask, Blueprint, request, render_template, redirect, url_for, flash, abort
from voteapp import db
from voteapp.models import Member, load_user
from flask_login import login_user, login_required, logout_user, current_user
'''
============================================================
                        STATS
============================================================
'''
'''
    sqlalchemy.engine.result.ResultProxy
    sqlalchemy.engine.result.RowProxy
    The keys and the values need to be in lists passed in separately.
'''
stats_blueprint = Blueprint('stats',
                              __name__,
                              template_folder='templates/stats', static_folder='static')

@stats_blueprint.route('/stats')
@login_required
def stats():
    data = []
    label = []
    sql = '''select members.name, members.id, count(*) AS "total"
    from members join votes on members.name = votes.userName
    group by members.name
    ORDER BY total desc'''
    resultList = db.engine.execute(sql)
    rows = resultList.fetchall()
    for i in rows:
        label.append(str(i[0]))
        data.append(i[2])
        print("data: ", data, file=sys.stderr)
    return render_template('stats.html', results = rows, label = label, data = data)

@stats_blueprint.route('/stats/<int:memberId>')
@login_required
def countVotes(memberId):
    data = []
    label = []
    sql = '''select voteName, count(*) as "total"
    from votes
    where memberId = ?
    group by voteName
    order by total desc, voteName
    '''
    resultList = db.engine.execute(sql, (memberId,))
    rows = resultList.fetchall()
    for i in rows:
        label.append(str(i[0]))
        data.append(i[1])
        print("data: ", data, file=sys.stderr)
    print("resultList: ", type(resultList), file=sys.stderr)
    member = load_user(memberId)
    return render_template('showlist.html', member = member, results = rows, label = label, data = data)
