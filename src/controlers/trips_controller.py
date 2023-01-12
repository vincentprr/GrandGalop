from ..core.database import db
from ..models.sortie import Sortie
from ..models.activite import Activite
from ..models.moniteur import Moniteur
from ..core.utils import MultiCheckboxField
from ..controlers.activities_controller import get_activities, get_activity_by_id
from ..controlers.user_controller import get_moniteurs, get_available_moniteurs_ids, get_moniteur_by_id
from flask_wtf import FlaskForm
from wtforms import SelectField, IntegerField, DateTimeLocalField
from wtforms.validators import DataRequired
from datetime import datetime

def get_trip_by_id(id:int) -> Sortie or None:
    return Sortie.query.get(id)

def get_trips(**kwargs) -> "list[Sortie]":
    return Sortie.query.filter_by(**kwargs).all()

def add_trip(activity:Activite, date:str, duree:int, moniteurs:"list[Moniteur]"):
    db.session.add(Sortie(
        activite=activity,
        date=date,
        duree=duree,
        moniteurs=moniteurs
    ))
    db.session.commit()

def del_trip(model:Sortie):
    db.session.delete(model)
    db.session.commit()

class AddTripForm(FlaskForm):
    activite = SelectField("Activité", validators=[DataRequired()], choices=[], render_kw={"class":"input input_register"})
    date = DateTimeLocalField("Date", validators=[DataRequired()], format='%Y-%m-%dT%H:%M', render_kw={"class":"input input_register"})
    duree = IntegerField("Durée de la sortie (min)", validators=[DataRequired()], render_kw={"class":"input input_register"})
    moniteur = MultiCheckboxField("Moniteurs", choices=[])

    def setup_choices(self):
        for activity in get_activities():
            self.activite.choices.append((str(activity.id), activity.nom))

        for moniteur in get_moniteurs():
            self.moniteur.choices.append((str(moniteur.id), moniteur.personne.prenom + ' ' + moniteur.personne.nom))

    def add(self):
        res = ""
        moniteurs = []
        availables_moniteurs = get_available_moniteurs_ids(self.date.data, self.duree.data)

        for moniteur_id in self.moniteur.data:
            moniteur = get_moniteur_by_id(int(moniteur_id))
            if moniteur:
                if moniteur.id in availables_moniteurs:
                    moniteurs.append(moniteur)
                else:
                    res = "Le moniteur "+ moniteur.personne.prenom + ' ' + moniteur.personne.nom +" n'est pas disponible durant cette periode..."
                    break 
            else:
                res = "Le moniteur "+ moniteur_id +" n'existe pas..."
                break

        if len(res) == 0:
            if len(moniteurs) > 0:
                activite = get_activity_by_id(int(self.activite.data))
                if activite:
                    if self.date.data > datetime.now():
                        add_trip(activite, self.date.data, self.duree.data, moniteurs)
                    else:
                        res = "Vous ne pouvez pas planifier une sortie à une date déjà passée..."
                else:
                    res = "L'activité sélectionné n'existe pas..."
            else:
                res = "Aucun moniteur n'a été selectionné..."

        return res