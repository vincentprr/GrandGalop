from ..core.database import db
from ..models.monter import Monter
from ..models.sortie import Sortie
from ..models.poney import Poney
from ..models.client import Client
from ..controlers.poney_controller import get_poney_by_id
from flask_wtf import FlaskForm
from wtforms import SelectField
from wtforms.validators import DataRequired
from datetime import datetime

def unsubscribe_cours(model:Monter):
    db.session.delete(model)
    db.session.commit()

def subscribe(trip:Sortie, user:Client, poney:Poney):
    db.session.add(Monter(
        sortie=trip,
        client=user,
        poney=poney
    ))
    db.session.commit()

class SubscribeForm(FlaskForm):
    poney = SelectField("Poney", validators=[DataRequired()], choices=[], render_kw={"class":"input input_register"})

    def setup_choices(self, available_poneys:"list[Poney]"):
        for poney in available_poneys:
            self.poney.choices.append((str(poney.id), poney.nom))

    def add(self, user:Client, sortie:Sortie, available_poneys:Poney):
        can_sub = True

        for monter in user.monter:
            if monter.sortie.id == sortie.id:
                can_sub = False
                break

        if can_sub:
            poney_free = False
            poney_int = int(self.poney.data)

            for poney in available_poneys:
                if poney_int == poney.id:
                    poney_free = True
                    break
            
            if poney_free and sortie.date > datetime.now():
                poney = get_poney_by_id(poney_int)
                if poney:
                    subscribe(sortie, user, poney)