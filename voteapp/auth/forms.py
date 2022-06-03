from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from voteapp.models import Member

class RegistrationForm(FlaskForm):
    '''
        Added validators DataRequired(), Email() EqualTo()
    '''
    name = StringField('Name: ', validators=[DataRequired()])
    password = PasswordField('Password: ', validators=[DataRequired(), EqualTo('pass_confirm', message='Passwords Must Match!')])
    pass_confirm = PasswordField('Confirm Password: ', validators=[DataRequired()])
    submit = SubmitField('Register')

    # Custom validator
    def checkName(self, name):
        # Check if not None for that user email!
        if Member.query.filter_by(name=name).first():
            raise ValidationError('The login name entered is already registered.')

class LoginForm(FlaskForm):
    name = StringField('Login: ', validators=[DataRequired()])
    password = PasswordField('Password: ', validators=[DataRequired()])
    submit = SubmitField('Login')
