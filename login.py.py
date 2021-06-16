import pymysql
from flask import Flask, render_template, url_for, flash, redirect, request
from forms import RegistrationForm, LoginForm, HomePage
from flask_login import LoginManager, UserMixin, login_user, current_user, logout_user

conn = pymysql.connect(host = '127.0.0.1', user = 'root', password = 'root' , database='xtipl')
cur = conn.cursor()

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title='home')


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    '''if current_user.is_authenticated:
        return redirect(url_for('home'))'''
    form = RegistrationForm()
    if form.validate_on_submit():
        if request.method == "POST":
            details = request.form

        cur.execute("INSERT INTO student(name,email,password) VALUES ('%s', '%s', '%s')" % (
        form.username.data, form.email.data, form.password.data))
        conn.commit()
        cur.close()

        flash(f'Registration Successful for {form.username.data}!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    '''if current_user.is_authenticated:
        return redirect(url_for('home'))'''
    form = LoginForm()
    if form.validate_on_submit():
        if request.method == "POST":
            count = cur.execute('SELECT * FROM student WHERE email = %s AND password = %s',
                                (form.email.data, form.password.data))
            conn.commit()
            # cur.close()
            if count:
                flash('{} You have been logged in!'.format(form.email.data), 'success')
                # login_user()
                return redirect(url_for('account'))
            else:
                flash('Login Unsuccessful. Please check username and password', 'danger')
        return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    #logout_user()
    return render_template('home')

@app.route("/account")
#@login_required
def account():
    return render_template('account.html', title='Account')


if __name__ == '__main__':
    app.run(debug=True)

