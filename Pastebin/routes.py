from Pastebin import app
from flask import render_template, redirect, url_for
from Pastebin.forms import Loginform, Registerform
from Pastebin import db
from Pastebin.models import User


@app.route('/')
@app.route('/login', method=['POST', 'GET'])
def login():
    form = Loginform()
    if form.validate_on_submit():
        login = User(username=form.username.data, password=form.password.data)
        db.session.add(login)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('index.html', form=form)


@app.route('/user', method=['POST', 'GET'])
def user():
    form = Registerform()
    if form.validate_on_submit():
        new_user = User(username=form.username.data,
                        password=form.password.data)
        db.session.add(login)
        db.session.commit()
        return redirect(url_for('user'))
    return render_template('user.html', form=format)
