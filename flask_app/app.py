from flask import Flask, render_template, request, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange
import os

app = Flask(__name__)
# Set a strong secret key for CSRF protection
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-key-please-change')
app.config['WTF_CSRF_ENABLED'] = True

class UserForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired(), NumberRange(min=0, max=120)])
    submit = SubmitField('Submit')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/greet', methods=['GET', 'POST'])
def greet():
    form = UserForm()
    if form.validate_on_submit():
        name = form.name.data
        age = form.age.data
        return render_template('greeting.html', name=name, age=age)
    return render_template('form.html', form=form)

if __name__ == '__main__':
    # Debug mode should be controlled by environment variable
    debug_mode = os.environ.get('FLASK_DEBUG', '0') == '1'
    app.run(host='0.0.0.0', port=5000, debug=debug_mode) 