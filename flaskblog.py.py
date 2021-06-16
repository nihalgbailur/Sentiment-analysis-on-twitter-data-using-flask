import pymysql
from flask import Flask, render_template, url_for, flash, redirect, request
from forms import RegistrationForm, LoginForm, HomePage
from get_tweets import TweetName
from flask_login import LoginManager, UserMixin, login_user, current_user, logout_user
from front_end_gui import File_Pass
import matplotlib.pyplot as plt


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
        
        cur.execute("INSERT INTO student(name,email,password) VALUES ('%s', '%s', '%s')" %(form.username.data, form.email.data, form.password.data))
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
            count = cur.execute("select name from student where email= '%s'" %form.email.data)
            conn.commit()
            cur.close()
            if count:
                flash('{} You have been logged in!'.format(form.email.data), 'success')

                return redirect(url_for('home'))
            else:
                flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/tweet_analyzer")
def tweet():
    form = HomePage()
    return render_template('tweet.html', title='tweet analyzer')

@app.route('/search',methods = ['POST', 'GET'])
def search():
   if request.method == 'POST':
      name = request.form['nm']
      getweet = TweetName(name)
      getweet.get_tweets()

      return render_template('search.html', title='browse file')


@app.route('/choose',methods = ['POST', 'GET'])
def choose():
    if request.method == 'GET':
        return render_template('load.html')

@app.route('/analyse', methods=['POST', 'GET'])
def analyse():
    if request.method == 'POST':
        f = request.files['file']
        name = f.filename
        obj = File_Pass(name)
        data_out = obj.Analysiz_Text()

        labels = 'positive_sentiment', 'negative_sentiment', 'neutral_sentiment',
        sizes = [data_out[0], data_out[1], data_out[2]]
        explode = (0.1, 0.1, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        fig1.savefig('static\my_plot.png')
        #plt.show()

        dict = {'Positive Sentiment': data_out[0], 'Negative Sentiment': data_out[1], 'Neutral Sentiment': data_out[2] }

        return render_template('display.html', result = dict)


if __name__ == '__main__':
    app.run(debug=True)
