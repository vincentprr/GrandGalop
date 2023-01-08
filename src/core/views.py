from flask import render_template, redirect, url_for
from markupsafe import Markup
from .app import app
from ..controlers.user_controller import LoginForm, RegisterForm, create_client
from flask_login import current_user, login_user, logout_user, login_required
from .utils import space_between

@app.route("/index")
@app.route("/accueil")
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/logout")
def logout():
    if current_user.is_authenticated:
        logout_user()

    return redirect(url_for("index"))

@app.route("/register", methods=["GET", "POST"])
def register():
    register_form = RegisterForm()
    callback = ""

    if register_form.validate_on_submit():
        callback = register_form.insert_client()
        if len(callback) == 0:
            callback = '<span class="form_callback_v">Votre compte a été créé avec succès !</span>'

    return render_template("register.html", register_form=register_form, callback=Markup(callback))

@app.route("/team")
def team():
    return render_template("team.html")

@app.route("/account")
@login_required
def account():
    return render_template("account.html", space_between=space_between)

# JS
@app.route("/js/main", methods=["GET", "POST"])
def main_js():
    login_form = LoginForm()

    if not current_user.is_authenticated:
        if login_form.validate_on_submit():
            user = login_form.get_authenticated_user()
            if user is not None:
                login_user(user)
                return redirect(url_for("index"))

    return render_template("js/main.js", loginForm=login_form)