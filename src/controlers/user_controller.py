from flask_wtf import FlaskForm
from wtforms import PasswordField, EmailField, StringField, TelField
from wtforms.validators import DataRequired, Length
from ..core.app import login_manager
from ..core.database import db
from ..models.client import Client
from hashlib import sha256
from datetime import datetime

@login_manager.user_loader
def get_client_by_id(id : int) -> Client or None:
    return Client.query.get(id)

def get_client(**kwargs) -> Client or None:
    return Client.query.filter_by(**kwargs).first()

def create_client(mail:str, password:str, name:str, last_name:str, tel:str, adr:str):
    h = sha256()
    h.update(password.encode())

    db.session.add(Client(
        email = mail,
        mdp = h.hexdigest(),
        prenom = name,
        nom = last_name,
        tel = tel,
        adr = adr,
        date_cotisation = datetime.utcnow()
    ))
    db.session.commit()

class LoginForm(FlaskForm):
    login = EmailField("Email", validators=[DataRequired()], render_kw={"class":"input input_login"})
    password = PasswordField("Mot de passe", validators=[DataRequired()], render_kw={"class":"input input_login"})

    def get_authenticated_user(self):
        user = get_client(email=self.login.data)
        hash = sha256()
        hash.update(self.password.data.encode())

        return user if user is not None and user.mdp == hash.hexdigest() else None

class RegisterForm(FlaskForm):
    nom = StringField("Nom", validators=[DataRequired()], render_kw={"class":"input input_register"})
    prenom = StringField("Prénom", validators=[DataRequired()], render_kw={"class":"input input_register"})
    email = EmailField("Email", validators=[DataRequired()], render_kw={"class":"input input_register"})
    mdp = PasswordField("Mot de passe", validators=[DataRequired()], render_kw={"class":"input input_register"})
    mdp_verif = PasswordField("Vérification du mot de passe", validators=[DataRequired()], render_kw={"class":"input input_register"})
    adr = StringField("Adresse", validators=[DataRequired()], render_kw={"class":"input input_register"})
    tel = TelField("Téléphone (ex: 06XXXXXXXX)", validators=[DataRequired(), Length(10, 10)], render_kw={"class":"input input_register"})

    def insert_client(self) -> str:
        res = ""
        if self.mdp.data == self.mdp_verif.data:
            create_client(self.email.data, self.mdp.data, self.prenom.data, self.nom.data, self.tel.data, self.adr.data)
        else:
            res = '<span class="form_callback_e">Les mots de passes ne correspondent pas...</span>'

        return res
