from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hello World!</h1>"

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('user', usr= user))
    else:
        return render_template('login.html')
@app.route("/<usr>")
def user(usr):
    return f"<h1> Hello {usr}!"
if __name__ == '__main__':
    app.run(debug=True)