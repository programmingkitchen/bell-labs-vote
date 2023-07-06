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

    TODO:  How do we make sure that only admin can do this?
    https://flask-login.readthedocs.io/en/latest/

    myuser = current_user.get_id()
    auth = current_user.is_authenticated
    active = current_user.is_active
    anon = current_user.is_anonymous

    print("Current User: ", current_user, file=sys.stderr)
    print("\tType: ", type(current_user), file=sys.stderr)
    print("\nMy User: ", myuser, file=sys.stderr)
    print("\tType: ", type(myuser), file=sys.stderr)
    print("\nDefaultsType: ", myuser, auth, active, anon, file=sys.stderr)

    delete from members
where id  != 1

delete from votes
'''
admin_blueprint = Blueprint('admin',
                              __name__,
                              template_folder='templates/admin', static_folder='static')

@admin_blueprint.route('/')
@login_required
def admin():
    myuser = int(current_user.get_id())
    auth = current_user.is_authenticated
    active = current_user.is_active
    anon = current_user.is_anonymous

    print("Current User: ", current_user, file=sys.stderr)
    print("\tType: ", type(current_user), file=sys.stderr)
    print("\nMy User: ", myuser, file=sys.stderr)
    print("\tType: ", type(myuser), file=sys.stderr)
    print("\nDefaultsType: ", myuser, auth, active, anon, file=sys.stderr)
    
    if myuser == 1:
        return render_template('admin.html')
    else:
        return render_template('error.html')


@admin_blueprint.route('/clear')
@login_required
def clear():
    sql = '''delete from votes'''
    try:
        resultList = db.engine.execute(sql)
        return render_template('admin.html')
    except:
        print("ERROR: clearing database.", file=sys.stderr)
        return render_template('admin.html')