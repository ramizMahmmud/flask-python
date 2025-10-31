from flask import Flask, redirect, session, render_template, url_for, request, flash
from datetime import timedelta
app = Flask(__name__)

app.secret_key = b"dfhakjfa"
# Permanent session
app.permanent_session_lifetime = timedelta(minutes=5)


@app.route('/')
def index():
    return render_template("home.html")


@app.route('/user')
def user():
    if "usr" in session:
        user = session["usr"]
        return render_template("user.html", user = user)
    else:
        return redirect(url_for("login"))


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        session.permanent = True
        user = request.form['nm']
        session["usr"] = user
        flash("Login Successful!")
        return redirect(url_for('user'))
    else:
        if "usr" in session:
            flash("You are already Logged in!")
            return redirect(url_for("user"))
        return render_template("login.html")

@app.route('/logout')
def logout():
    session.pop("usr", None)
    flash("Logged Out Successfully")
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)