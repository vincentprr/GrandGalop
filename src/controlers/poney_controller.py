from ..core.database import db
from ..models.poney import Poney
from ..models.sortie import Sortie
from ..core.constant import HORSE_SLEEP_TIME
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import StringField, FloatField, DateField, FileField
from wtforms.validators import DataRequired
from datetime import timedelta, datetime

def get_poney_by_id(id) -> Poney:
    return Poney.query.get(id)

def get_poneys(**kwargs) -> "list[Poney]":
    return Poney.query.filter_by(**kwargs).all()

def get_available_poneys(sortie:Sortie):
    res = []
    now = datetime.now()

    for poney in get_poneys():
        add = True

        if len(poney.monter) > 0:
            monter = poney.monter.sort(key=lambda x: x.sortie.date + timedelta(minutes=x.sortie.duree))[0]
            if monter.sortie.date + timedelta(minutes=monter.sortie.duree, hours=HORSE_SLEEP_TIME) > now:
                add = False
                break

        if add:
            res.append(poney)
    
    return res

def create_poney(nom:str, charge_max:int, date_naissance:str, taille:int, img:str):
    db.session.add(Poney(
        nom = nom,
        charge_max = charge_max,
        date_naissance = date_naissance,
        taille = taille,
        img = img
    ))
    db.session.commit()

def del_poney(model:Poney):
    db.session.delete(model)
    db.session.commit()

class AddPoneyForm(FlaskForm):
    nom = StringField("Nom", validators=[DataRequired()], render_kw={"class":"input input_register"})
    charge_max = FloatField("Charge maximale en kg", validators=[DataRequired()], render_kw={"class":"input input_register"})
    date_naissance = DateField("Date de naissance", validators=[DataRequired()], render_kw={"class":"input input_register"})
    taille = FloatField("Taille en m", validators=[DataRequired()], render_kw={"class":"input input_register"})
    img = FileField("Image", validators=[FileAllowed(['jpg', 'png'], 'Images only!')])

    def create_poney(self, request):
        create_poney(self.nom.data, int(self.charge_max.data * 1000), self.date_naissance.data, int(self.taille.data * 100), request.files[(self.img.name)].read())

class EditPoneyForm(FlaskForm):
    nom = StringField("Nom", validators=[DataRequired()], render_kw={"class":"input input_register"})
    charge_max = FloatField("Charge maximale en kg", validators=[DataRequired()], render_kw={"class":"input input_register"})
    date_naissance = DateField("Date de naissance", validators=[DataRequired()], render_kw={"class":"input input_register"})
    taille = FloatField("Taille en m", validators=[DataRequired()], render_kw={"class":"input input_register"})

    def edit_poney(self, poney:Poney):
        poney.nom = self.nom.data
        poney.charge_max = int(self.charge_max.data * 1000)
        poney.date_naissance = self.date_naissance.data
        poney.taille = int(self.taille.data * 100)
        db.session.commit()