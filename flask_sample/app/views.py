from app import app
from flask import render_template, flash, redirect
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname' : 'admin'} #fake user
    return render_template('index.html',
                    title = 'Home',
                    user = user)

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for Openid="%s", remember me:"%s" ' % (form.openid.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html',title='Sign in',form = form)