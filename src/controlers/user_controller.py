from flask_wtf import FlaskForm
from wtforms import PasswordField, EmailField, StringField, TelField, SelectField, FileField
from flask_wtf.file import FileAllowed
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
from ..core.constant import TYPE_CLIENT, TYPE_MONITEUR, TYPE_ADMIN
from datetime import datetime, timedelta

@login_manager.user_loader
def get_personne_by_id(id : int) -> Personne or None:
    return Personne.query.get(id)

def get_personne(**kwargs) -> Client or None:
    return Personne.query.filter_by(**kwargs).first()

def get_personnes(**kwargs) -> "list[Personne]":
    return Personne.query.filter_by(**kwargs).all()

def get_admins(**kwargs) -> "list[Admin]":
    return Admin.query.filter_by(**kwargs).all()

def get_moniteur_by_id(id : int) -> Moniteur or None:
    return Moniteur.query.get(id)

def get_moniteurs(**kwargs) -> "list[Moniteur]":
    return Moniteur.query.filter_by(**kwargs).all()

def get_available_moniteurs_ids(date:datetime, duree:int) -> "list[int]":
    res = set()
    end_act_date = date + timedelta(minutes=duree)

    for moniteur in get_moniteurs():
        add = True
        for sortie in moniteur.sorties:
            end_datetime = sortie.date + timedelta(minutes=sortie.duree)
            if (date >= sortie.date and date <= end_datetime) or (end_act_date >= sortie.date and end_act_date <= end_datetime):
                add = False
                break
        if add:
            res.add(moniteur.id)

    return res

def create_personne(mail:str, password:str, name:str, last_name:str, tel:str, adr:str) -> Personne:
    personne = Personne(
        email = mail,
        mdp = crypt(password),
        prenom = name,
        nom = last_name,
        tel = tel,
        adr = adr,
    )
    db.session.add(personne)
    db.session.commit()

    return personne

def create_client(mail:str, password:str, name:str, last_name:str, tel:str, adr:str):
    p = create_personne(mail, password, name, last_name, tel, adr)
    db.session.add(Client(
        id = p.id,
        date_cotisation = datetime.utcnow()
    ))
    db.session.commit()

def create_moniteur(mail:str, password:str, name:str, last_name:str, tel:str, adr:str, img=None):
    p = create_personne(mail, password, name, last_name, tel, adr)
    db.session.add(Moniteur(
        id = p.id,
        img=img
    ))
    db.session.commit()

def create_admin(mail:str, password:str, name:str, last_name:str, tel:str, adr:str, img=None):
    p = create_personne(mail, password, name, last_name, tel, adr)
    db.session.add(Admin(
        id = p.id,
        img=img
    ))
    db.session.commit()

def del_user(user:Personne):
    if user.client:
        db.session.delete(user.client)
    if user.moniteur:
        db.session.delete(user.moniteur)
    if user.admin:
        db.session.delete(user.admin)
    db.session.commit()

    db.session.delete(user)
    db.session.commit()

class LoginForm(FlaskForm):
    login = EmailField("Email", validators=[DataRequired()], render_kw={"class":"input input_login"})
    password = PasswordField("Mot de passe", validators=[DataRequired()], render_kw={"class":"input input_login"})

    def get_authenticated_user(self) -> Personne or None:
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
            if get_personne(email=self.email.data) == None:
                create_client(self.email.data, self.mdp.data, self.prenom.data, self.nom.data, self.tel.data, self.adr.data)
            else:
                res = '<span class="form_callback_e">Un compte utilise déjà cette adresse mail...</span>'
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

class AddUserForm(FlaskForm):
    nom = StringField("Nom", validators=[DataRequired()], render_kw={"class":"input input_register"})
    prenom = StringField("Prénom", validators=[DataRequired()], render_kw={"class":"input input_register"})
    email = EmailField("Email", validators=[DataRequired()], render_kw={"class":"input input_register"})
    mdp = PasswordField("Mot de passe", validators=[DataRequired(), Length(4)], render_kw={"class":"input input_register"})
    adr = StringField("Adresse", validators=[DataRequired()], render_kw={"class":"input input_register"})
    tel = TelField("Téléphone (ex: 06XXXXXXXX)", validators=[DataRequired(), Length(10, 10)], render_kw={"class":"input input_register"})
    user_type = SelectField("Type d'utilisateur", choices=[(TYPE_CLIENT, "Client"), (TYPE_MONITEUR, "Moniteur"), (TYPE_ADMIN, "Administration")], render_kw={"class":"input input_register"})
    img = FileField("Image", validators=[FileAllowed(['jpg', 'png'], 'Images only!')], render_kw={"style":"display: none;"})

    def add_user(self, request) -> str:
        res = ""
        if get_personne(email=self.email.data) == None:
            int_user_type = int(self.user_type.data)
            if int_user_type == TYPE_CLIENT:
                create_client(self.email.data, self.mdp.data, self.prenom.data, self.nom.data, self.tel.data, self.adr.data)
            elif int_user_type == TYPE_MONITEUR:
                create_moniteur(self.email.data, self.mdp.data, self.prenom.data, self.nom.data, self.tel.data, self.adr.data, request.files[(self.img.name)].read())
            elif int_user_type == TYPE_ADMIN:
                create_admin(self.email.data, self.mdp.data, self.prenom.data, self.nom.data, self.tel.data, self.adr.data, request.files[(self.img.name)].read())
            else:
                res = '<span class="form_callback_e">Type d\'utilisateur incorrect...</span>'
        else:
            res = '<span class="form_callback_e">Un compte utilise déjà cette adresse mail...</span>'

        return res

class EditUserForm(FlaskForm):
    nom = StringField("Nom", validators=[DataRequired()], render_kw={"class":"input input_register"})
    prenom = StringField("Prénom", validators=[DataRequired()], render_kw={"class":"input input_register"})
    email = EmailField("Email", validators=[DataRequired()], render_kw={"class":"input input_register"})
    mdp = PasswordField("Mot de passe (optionnel)", render_kw={"class":"input input_register"})
    adr = StringField("Adresse", validators=[DataRequired()], render_kw={"class":"input input_register"})
    tel = TelField("Téléphone (ex: 06XXXXXXXX)", validators=[DataRequired(), Length(10, 10)], render_kw={"class":"input input_register"})

    def edit_user(self, personne) -> str:
        res = ""
        if personne.email == self.email.data or get_personne(email=self.email.data) == None:
            personne.nom = self.nom.data
            personne.prenom = self.prenom.data
            personne.email = self.email.data
            personne.adr = self.adr.data
            personne.tel = self.tel.data
            if len(self.mdp.data) > 3:
                personne.mdp = crypt(self.mdp.data)
            
            db.session.commit()
        else:
            res = '<span class="form_callback_e">Un compte utilise déjà cette adresse mail...</span>'

        return res
