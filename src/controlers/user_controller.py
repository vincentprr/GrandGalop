from flask_wtf import FlaskForm
from wtforms import PasswordField, EmailField, StringField, TelField
from wtforms.validators import DataRequired, Length
from ..core.app import login_manager
from ..core.database import db
from ..models.client import Client
from ..models.personne import Personne
from ..models.admin import Admin
from ..models.moniteur import Moniteur
from ..core.utils import crypt
from datetime import datetime
from flask_login import current_user

@login_manager.user_loader
def get_personne_by_id(id : int) -> Personne or None:
    return Personne.query.get(id)

def get_personne(**kwargs) -> Client or None:
    return Personne.query.filter_by(**kwargs).first()

def get_admins(**kwargs) -> "list[Admin]":
    return Admin.query.filter_by(**kwargs).all()

def get_moniteurs(**kwargs) -> "list[Moniteur]":
    return Moniteur.query.filter_by(**kwargs).all()

def create_personne(mail:str, password:str, name:str, last_name:str, tel:str, adr:str):
    db.session.add(Personne(
        email = mail,
        mdp = crypt(password),
        prenom = name,
        nom = last_name,
        tel = tel,
        adr = adr,
    ))
    db.session.commit()

def create_client(mail:str, password:str, name:str, last_name:str, tel:str, adr:str):
    create_personne(mail, password, name, last_name, tel, adr)
    db.session.add(Client(
        date_cotisation = datetime.utcnow()
    ))
    db.session.commit()

class LoginForm(FlaskForm):
    login = EmailField("Email", validators=[DataRequired()], render_kw={"class":"input input_login"})
    password = PasswordField("Mot de passe", validators=[DataRequired()], render_kw={"class":"input input_login"})

    def get_authenticated_user(self):
        user = get_personne(email=self.login.data)

        return user if user is not None and user.mdp == crypt(self.password.data) else None

class RegisterForm(FlaskForm):
    nom = StringField("Nom", validators=[DataRequired()], render_kw={"class":"input input_register"})
    prenom = StringField("Prénom", validators=[DataRequired()], render_kw={"class":"input input_register"})
    email = EmailField("Email", validators=[DataRequired()], render_kw={"class":"input input_register"})
    mdp = PasswordField("Mot de passe", validators=[DataRequired(), Length(4)], render_kw={"class":"input input_register"})
    mdp_verif = PasswordField("Vérification du mot de passe", validators=[DataRequired(), Length(4)], render_kw={"class":"input input_register"})
    adr = StringField("Adresse", validators=[DataRequired()], render_kw={"class":"input input_register"})
    tel = TelField("Téléphone (ex: 06XXXXXXXX)", validators=[DataRequired(), Length(10, 10)], render_kw={"class":"input input_register"})

    def insert_client(self) -> str:
        res = ""
        if self.mdp.data == self.mdp_verif.data:
            create_client(self.email.data, self.mdp.data, self.prenom.data, self.nom.data, self.tel.data, self.adr.data)
        else:
            res = '<span class="form_callback_e">Les mots de passes ne correspondent pas...</span>'

        return res

class EditAccountForm(FlaskForm):
    adr = StringField("Adresse", validators=[DataRequired()], render_kw={"class":"input input_register"})
    tel = TelField("Téléphone (ex: 06XXXXXXXX)", validators=[DataRequired(), Length(10, 10)], render_kw={"class":"input input_register"})
    mdp = PasswordField("Mot de passe", validators=[DataRequired(), Length(4)], render_kw={"class":"input input_register"})
    mdp_verif = PasswordField("Vérification du mot de passe", validators=[DataRequired(), Length(4)], render_kw={"class":"input input_register"})

    def edit_informations(self) -> str:
        res = ""
        if self.mdp.data == self.mdp_verif.data:
            current_user.adr = self.adr.data
            current_user.tel = self.tel.data
            current_user.mdp = crypt(self.mdp.data)
            db.session.commit()
        else:
            res = '<span class="form_callback_e">Les mots de passes ne correspondent pas...</span>'

        return res

