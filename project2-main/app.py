from flask import Flask, render_template, redirect, url_for,request,session
app = Flask(__name__,template_folder='',static_folder='')
from db import get_all_news,add_news, get_news_by_id

app = Flask(__name__, template_folder='', static_folder='')





@app.route("/")
def index():
    print(get_all_news())
    return render_template('home.html',news=get_all_news())


@app.route("/home/<id>")
def home(id):
    news = get_news_by_id(id)
    if news:
        return render_template('news.html',showed_news=news)
        

    
    return redirect('/')

@app.route("/auth/sign-in",methods=['GET','POST'])
def sign_in():
    if request.method == 'POST':
        if request.form['username'] == 'admin' and request.form['password'] == 'admin':
            return redirect('/')
        else:

            return render_template('sign-in.html',incorrect_password = True)
        
    return render_template('sign-in.html', incorrect_password=False)



@app.route("/auth/sign-up")
def sign_up():
    return render_template('sign-up.html')





app.run(debug=True)
