from flask_wtf import FlaskForm
from wtforms import StringFiled, TextAreaField, BooleanField
from wtforms.validators import DataRequired

class TodoForm(FlaskForm):
    title = StringFiled('title')
    descryption = TextAreaField('descryption')
    completed = BooleanField('completed') 