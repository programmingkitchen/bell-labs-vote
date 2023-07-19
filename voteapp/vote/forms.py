from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField,
                    SelectField, TextField, TextAreaField, RadioField, SubmitField)
from wtforms.validators import DataRequired


class VoteForm(FlaskForm):
    show = RadioField(u'Show New',
    choices=[('Information Theory', 'Shannon & Information Theory'),
    ('Cryptography', 'Shannon & Cryptography'),
    ('MUSIC', 'Mathews & MUSIC'),
    ('Source Code Control', 'Rochkind(Source Code Control)'),
    ('Computer Animation', 'Sinden et. al.(Computer Animation)'),
    ('Error Detection & Correction', 'Error Detection & Correction(Hamming)'),
    ('C Language', 'Kernighan & Ritchie(C)'),
    ('UNIX', 'Kernighan & Ritchie(UNIX)'),
    ('The Transitor', 'Bardeen, Brattain & Shockley (Transistor)'),
    ('Theory of Everything', 'Theory of Everything(Dr. Jerry Robinson)')], default='Theory of Everything')
    submit = SubmitField('Vote')
