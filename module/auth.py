from flask import Blueprint,render_template,url_for,redirect,request,flash
from models import User
from extensions import db

from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import login_user, login_required, logout_user




auth = Blueprint("auth",__name__)




@auth.route("/login")
def login():
	return render_template("login.html")


@auth.route("/login",methods=["POST"])
def login_post():
	if request.method == "POST":
		username = request.form.get("user")
		password = request.form.get("password")
		remember = request.form.get("remember")

		user = User.query.filter_by(username=username).first()

		if not user or not check_password_hash(user.password,password):
			flash("Please check your login details and try again")
			return redirect(url_for('auth.login'))
		login_user(user,remember=remember)
		return redirect(url_for('index'))


@auth.route("/signup")
def signup():
	return  render_template("signup.html")

@auth.route("/signup",methods=["POST"])
def signup_post():
	email = request.form.get("email")
	username = request.form.get("user")
	password = request.form.get("password")

	user = User.query.filter_by(username=username).first()
	if user:
		return redirect(url_for("login"))

	new_user = User(email=email,username=username,password=generate_password_hash(password,method='sha256'))

	db.session.add(new_user)
	db.session.commit()

	login_user(new_user)

	return redirect(url_for("index"))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home_page'))

