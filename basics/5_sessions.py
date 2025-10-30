from flask import Flask, redirect,render_template, request, url_for, session

app = Flask(__name__)

app.secret_key = b'asdhfgajw'


@app.route('/')
def home():
    return "<h1>Hello</h1>"

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        session["user"] = user
        return redirect(url_for("user"))
    return render_template('login.html')

@app.route('/user')
def user():
    if "user" in session:
        user = session["user"]
        return f"<h1>{user}</h1>"
    else:
        return redirect(url_for("login"))

@app.route('/logout')
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)