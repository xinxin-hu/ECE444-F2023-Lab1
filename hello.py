from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired,Email,InputRequired,Regexp
import email_validator

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a string nobody knows'
bootstrap = Bootstrap(app)
moment = Moment(app)

class NameAndEmailForm (FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()]) # 'name' is used when rendering form to HTML
    email =StringField('What is your UofT Email address?',validators=[Email()])
    submit = SubmitField('Submit')
@app.route('/', methods=['GET', 'POST']) #when methods not specified, takes 'GET' method only
def index():
    form = NameAndEmailForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        old_email = session.get('email')
        uoftEmail = 'utoronto'
        if old_name != None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        if old_email != None and old_email != form.email.data:
            flash('Looks like you have changed your email!')
        if uoftEmail in form.email.data:
            session['uoftEmail'] = True
        session['name'] = form.name.data
        session['email'] = form.email.data
        form.name.data = ' '
        form.email.data = ' '
        return redirect(url_for('index')) # url_for takes the endpoint name as required argument, by default is the name of the view function attached to the route
    return render_template('index.html',form=form, name=session.get('name'), email= session.get('email'),
                           uoftEmail = session.get('uoftEmail'))
@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name, current_time=datetime.utcnow())
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ =='__main__':
    app.run()