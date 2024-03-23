from flask import Flask, render_template, redirect, url_for, request, session
app = Flask(__name__, template_folder='', static_folder='')
from db import get_all_news, add_news, get_news_by_id

@app.route("/")
def index():
    print(get_all_news())
    return render_template('home.html', news=get_all_news())

@app.route("/about/us")
def index2():
    return render_template('about_us.html')

@app.route("/home/<id>")
def home(id):
    news = get_news_by_id(id)
    if news:
        return render_template('news.html', showed_news=news)

    
    return redirect('/')


@app.route("/auth/sign-in", methods=["GET", "POST"])
def signIn():
    if request.method == "POST":
        if request.form['username'] == 'color' and request.form['password'] == '#ffff':
            session['user'] = True
            session['inccorect_pass'] = False
            return redirect('/profile')
        else:
            session['inccorect_pass'] = True
            return redirect(url_for('signIn'))
            
    if ('inccorect_pass' in session.keys()  ):
        return render_template('sign-in.html', incorrect_password=session['inccorect_pass'])
    
    return render_template('sign-in.html', incorrect_password=False)

@app.route("/auth/sign-up")
def signUp():
    return render_template('sign-in.html')




app.secret_key = 'secret'

app.run(debug=True)
