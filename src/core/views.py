from flask import render_template, redirect, url_for, request
from markupsafe import Markup
from .app import app
from ..controlers.activities_controller import get_activities_type, EditTypeActiviteForm, get_activity_type_by_id, del_activity_type, AddTypeActivity, get_activities, AddActivityForm, get_activity_by_id, del_activity, EditActivityForm
from ..controlers.user_controller import LoginForm, RegisterForm, EditAccountForm, get_admins, get_moniteurs, get_personnes, AddUserForm, get_personne_by_id, del_user, EditUserForm
from ..controlers.poney_controller import get_poneys, AddPoneyForm, del_poney, get_poney_by_id, EditPoneyForm
from ..controlers.trips_controller import get_trips, AddTripForm, get_trip_by_id, del_trip
from flask_login import current_user, login_user, logout_user, login_required
from .utils import space_between
from datetime import date
from .constant import TYPE_CLIENT
from datetime import datetime

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
    return render_template("team.html", admins=get_admins(), moniteurs=get_moniteurs())

@app.route("/account")
@login_required
def account():
    return render_template("account.html", space_between=space_between)

@app.route("/account/edit", methods=["GET", "POST"])
@login_required
def edit_account():
    edit_account_form = EditAccountForm()
    callback = ""

    if edit_account_form.validate_on_submit():
        callback = edit_account_form.edit_informations()

        if len(callback) == 0:
            return redirect(url_for("account"))

    return render_template("account_edit.html", edit_account_form=edit_account_form, callback=Markup(callback))


@app.route("/admin")
@login_required
def admin():
    if not current_user.admin:
        return redirect(url_for("index"))
    
    return render_template("admin.html")

@app.route("/poneys")
@login_required
def poneys():
    if not current_user.admin:
        return redirect(url_for("index"))

    return render_template("poneys.html", poneys=get_poneys(), today=date.today())

@app.route("/poneys/add", methods=["GET", "POST"])
@login_required
def add_poney():
    if not current_user.admin:
        return redirect(url_for("index"))

    add_poney_form = AddPoneyForm()

    if add_poney_form.validate_on_submit():
        add_poney_form.create_poney(request)
        return redirect(url_for("poneys"))
    
    return render_template("add_poney.html", add_poney_form=add_poney_form)

@app.route("/poneys/delete/<int:id>")
@login_required
def delete_poney(id):
    if not current_user.admin:
        return redirect(url_for("index"))

    poney = get_poney_by_id(id)
    if poney:
        del_poney(poney)

    return redirect(url_for("poneys"))

@app.route("/poneys/edit/<int:id>", methods=["GET", "POST"])
@login_required
def edit_poney(id):
    if not current_user.admin:
        return redirect(url_for("index"))
    
    poney = get_poney_by_id(id)

    if poney:
        edit_form = EditPoneyForm()

        if edit_form.validate_on_submit():
            edit_form.edit_poney(poney)

            return redirect(url_for("poneys"))

        return render_template("edit_poney.html", poney=poney, edit_form=edit_form)

    return redirect(url_for("index"))

@app.route("/users")
@login_required
def users():
    if not current_user.admin:
        return redirect(url_for("index"))

    return render_template("users.html", users=get_personnes(), space_between=space_between)

@app.route("/users/add", methods=["GET", "POST"])
@login_required
def add_user():
    if not current_user.admin:
        return redirect(url_for("index"))

    add_user_form = AddUserForm()
    callback = ""

    if add_user_form.validate_on_submit():
        callback = add_user_form.add_user(request)
        if len(callback) == 0:
            return redirect(url_for("users"))
    
    return render_template("add_user.html", add_user_form=add_user_form, callback=callback)

@app.route("/users/delete/<int:id>")
@login_required
def delete_user(id):
    if not current_user.admin:
        return redirect(url_for("index"))

    user = get_personne_by_id(id)
    if user:
        del_user(user)

    return redirect(url_for("users"))

@app.route("/users/edit/<int:id>", methods=["GET", "POST"])
@login_required
def edit_user(id):
    if not current_user.admin:
        return redirect(url_for("index"))
    
    user = get_personne_by_id(id)

    if user:
        edit_form = EditUserForm()
        callback = ""

        if edit_form.validate_on_submit():
            callback = edit_form.edit_user(user)
            if len(callback) == 0:
                return redirect(url_for("users"))

        return render_template("edit_user.html", user=user, edit_form=edit_form, callback=callback)

    return redirect(url_for("index"))

@app.route("/activities")
@login_required
def activities():
    if not current_user.admin:
        return redirect(url_for("index"))

    return render_template("activities.html")

@app.route("/activities/type")
@login_required
def activities_type():
    if not current_user.admin:
        return redirect(url_for("index"))

    return render_template("activities_type.html", types=get_activities_type())

@app.route("/activities/type/edit/<int:id>", methods=["GET", "POST"])
@login_required
def activities_type_edit(id):
    if not current_user.admin:
        return redirect(url_for("index"))

    type = get_activity_type_by_id(id)

    if type:
        edit_form = EditTypeActiviteForm()

        if edit_form.validate_on_submit():
            edit_form.edit(type)
            return redirect(url_for("activities_type"))

        return render_template("edit_activity_type.html", type=type, edit_form=edit_form)
    
    return redirect(url_for("index"))

@app.route("/activities/type/delete/<int:id>")
@login_required
def delete_activity_type(id):
    if not current_user.admin:
        return redirect(url_for("index"))

    type = get_activity_type_by_id(id)
    if type and len(type.activites) == 0:
        del_activity_type(type)

    return redirect(url_for("activities_type"))

@app.route("/activities/type/add", methods=["GET", "POST"])
@login_required
def add_activity_type():
    if not current_user.admin:
        return redirect(url_for("index"))

    add_type_form = AddTypeActivity()

    if add_type_form.validate_on_submit():
        add_type_form.add()
        return redirect(url_for("activities_type"))
    
    return render_template("add_activity_type.html", add_type_form=add_type_form)

@app.route("/activities/all")
@login_required
def activities_list():
    if not current_user.admin:
        return redirect(url_for("index"))

    return render_template("activities_.html", activities=get_activities())

@app.route("/activities/add", methods=["GET", "POST"])
@login_required
def add_activity():
    if not current_user.admin:
        return redirect(url_for("index"))

    add_form = AddActivityForm()
    add_form.setup_choices()

    if add_form.validate_on_submit():
        add_form.add()
        return redirect(url_for("activities_list"))
    
    return render_template("add_activity.html", add_form=add_form)

@app.route("/activities/delete/<int:id>")
@login_required
def delete_activity(id):
    if not current_user.admin:
        return redirect(url_for("index"))

    activity = get_activity_by_id(id)
    if activity:
        del_activity(activity)

    return redirect(url_for("activities_list"))

@app.route("/activities/edit/<int:id>", methods=["GET", "POST"])
@login_required
def activities_edit(id):
    if not current_user.admin:
        return redirect(url_for("index"))

    activity = get_activity_by_id(id)

    if activity:
        edit_form = EditActivityForm()
        edit_form.setup_choices(activity)
        edit_form.description.data = activity.description

        if edit_form.validate_on_submit():
            edit_form.edit(activity)
            return redirect(url_for("activities_list"))

        return render_template("edit_activity.html", activity=activity, edit_form=edit_form)
    
    return redirect(url_for("index"))

@app.route("/trips")
@login_required
def trips():
    if not current_user.admin:
        return redirect(url_for("index"))

    return render_template("trips.html", trips=get_trips())

@app.route("/trips/add", methods=["GET", "POST"])
@login_required
def add_trip():
    if not current_user.admin:
        return redirect(url_for("index"))

    callback = ""
    add_form = AddTripForm()
    add_form.setup_choices()

    if add_form.validate_on_submit():
        callback = add_form.add()
        if len(callback) == 0:
            return redirect(url_for("trips"))
    
    return render_template("add_trip.html", add_form=add_form, callback=callback)

@app.route("/trips/delete/<int:id>")
@login_required
def delete_trip(id):
    if not current_user.admin:
        return redirect(url_for("index"))

    trip = get_trip_by_id(id)
    if trip:
        del_trip(trip)
    
    return redirect(url_for("trips"))

@app.route("/planning")
@login_required
def planning():
    if not current_user.moniteur:
        return redirect(url_for("index"))

    return render_template("planning.html", now=datetime.now())

# JS
@app.route("/js/main", methods=["GET", "POST"])
def main_js():
    login_form = LoginForm()

    if login_form.validate_on_submit():
        if not current_user.is_authenticated:
            user = login_form.get_authenticated_user()
            if user is not None:
                login_user(user)
        
        return redirect(url_for("index"))


    return render_template("js/main.js", loginForm=login_form, TYPE_CLIENT=TYPE_CLIENT)