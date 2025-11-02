from flask import Flask, redirect, session, render_template, url_for, request, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.secret_key = b"sdihfauie"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.permanent_session_lifetime = timedelta(minutes=5)



# Initialize database
db = SQLAlchemy(app)

# create database class
class USERS(db.Model):
    _id = db.Column("id", db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/view")
def view():
    return render_template("view.html", values=USERS.query.all())

@app.route("/user", methods=["POST", "GET"])
def user():
    email = None
    if "user" in session:
        user = session["user"]
        if request.method == "POST":
            email = request.form["email"]
            session["email"] = email
            found_user = USERS.query.filter_by(name=user).first()
            found_user.email = email
            db.session.commit()
            
            flash(f"Hello {found_user.name}, your email has been updated to {email}!", "success")
            return "HELLO" #redirect(url_for("user"))  # redirect to avoid resubmitting on refresh
        else:
            if "email" in session:
                email = session["email"]
            return "ELSE"#render_template("user.html", email=email)
    else:
        return redirect(url_for("login"))

@app.route("/login", methods = ["POST", "GET"])
def login():
    session.permanent = True
    if request.method == "POST":
        user = request.form["nm"]
        session["user"] = user
        found_user = USERS.query.filter_by(name = user).first()
        if found_user:
            session["email"] = found_user.email
           
        else:
            usr = USERS(name = user, email = "")
            db.session.add(usr)
            db.session.commit()
        
        return redirect(url_for("user"))
    else:
        return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)