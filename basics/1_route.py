from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello world! <h1>HELLO</h1>'

@app.route('/<name>')
def user(name):
    return f"Hello {name}"

@app.route('/admin')
def admin():
    return redirect(url_for('home'))

@app.route('/subsriber')
def subscriber():
    return redirect(url_for('user', name = "Subscriber"))

if __name__== "__main__":
    app.run()