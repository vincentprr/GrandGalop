from ..core.database import db
from ..models.type_activite import TypeActivite
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

def get_activity_type_by_id(id:int) -> TypeActivite:
    return TypeActivite.query.get(id)

def get_activities_type(**kwargs) -> "list[TypeActivite]":
    return TypeActivite.query.filter_by(**kwargs).all()

def del_activity_type(model:TypeActivite):
    db.session.delete(model)
    db.session.commit()

def create_activity_type(name:str):
    db.session.add(TypeActivite(
        nom = name
    ))
    db.session.commit()

class AddTypeActivity(FlaskForm):
    nom = StringField("Nom", validators=[DataRequired()], render_kw={"class":"input input_register"})

    def add(self):
        create_activity_type(self.nom.data)

class EditTypeActiviteForm(FlaskForm):
    nom = StringField("Nom", validators=[DataRequired()], render_kw={"class":"input input_register"})

    def edit(self, type:TypeActivite):
        type.nom = self.nom.data
        db.session.commit()