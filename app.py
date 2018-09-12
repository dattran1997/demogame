from flask import Flask, render_template, redirect, request, session, url_for
import mlab
from mongoengine import *
from models.user import User
app = Flask(__name__)


mlab.connect()
app.secret_key = "this is a super secret_key"

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/login",methods =  ["GET","POST"])
def login():
    if request.method == "GET":
        return render_template('login.html')
    elif request.method == "POST":
        form = request.form
        username = form["username"]
        password = form["password"]
        user_found = User.objects(username = username, password = password)
        print(type(user_found))

        if user_found:
            session["logged_in"] = True
            accepted_user = User.objects.get(username = username, password = password)
            # for accepted_user in user_found:
            session["accepted_user"] = str(accepted_user.id)
            session["username"] = str(accepted_user.username)
            return redirect(url_for("index"))
        else:
            return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session["logged_in"] = False
    session.clear()
    return redirect(url_for("index"))

@app.route("/register",methods = ["GET","POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    elif request.method == "POST":
        form = request.form
        username = form["username"]
        password = form["password"]
        email = form["email"]
        new_user = User(username = username, password = password, email = email)
        new_user.save()
        return redirect(url_for("login"))

if __name__ == '__main__':
  # app.run(debug=True)
  app.run(debug=False)
