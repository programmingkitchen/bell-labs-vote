from flask import Flask, Blueprint, request, render_template, redirect, url_for

main_blueprint = Blueprint('main',
                              __name__,
                              template_folder='templates/main')



@main_blueprint.route('/')
def index():
    return redirect(url_for('auth.login'))
    #return redirect('/auth/login')
