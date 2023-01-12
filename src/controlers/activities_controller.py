from ..core.database import db
from ..models.type_activite import TypeActivite
from ..models.activite import Activite
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, IntegerField
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

def get_activity_by_id(id:int) -> Activite:
    return Activite.query.get(id)

def get_activities(**kwargs) -> Activite:
    return Activite.query.filter_by(**kwargs).all()

def create_activity(nom:str, description:str, max_clients:int, type_activite:TypeActivite):
    db.session.add(Activite(
        nom = nom,
        description = description,
        max_clients = max_clients,
        type_activite = type_activite
    ))
    db.session.commit()

def del_activity(model:Activite):
    db.session.delete(model)
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

class AddActivityForm(FlaskForm):
    nom = StringField("Nom", validators=[DataRequired()], render_kw={"class":"input input_register"})
    description = TextAreaField("Description", validators=[DataRequired()], render_kw={"class":"input input_register"})
    max_clients = IntegerField("Nombre maximum de clients", validators=[DataRequired()], render_kw={"class":"input input_register"})
    type_activite = SelectField("Type d'utilisateur", validators=[DataRequired()], choices=[], render_kw={"class":"input input_register"})

    def setup_choices(self):
        for type in get_activities_type():
            self.type_activite.choices.append((str(type.id), type.nom))

    def add(self):
        type = get_activity_type_by_id(int(self.type_activite.data))
        if type:
            create_activity(self.nom.data, self.description.data, self.max_clients.data, type)

class EditActivityForm(FlaskForm):
    nom = StringField("Nom", validators=[DataRequired()], render_kw={"class":"input input_register"})
    description = TextAreaField("Description", validators=[DataRequired()], render_kw={"class":"input input_register"})
    max_clients = IntegerField("Nombre maximum de clients", validators=[DataRequired()], render_kw={"class":"input input_register"})
    type_activite = SelectField("Type d'utilisateur", validators=[DataRequired()], choices=[], render_kw={"class":"input input_register"})

    def setup_choices(self, activity:Activite):
        for type in get_activities_type():
            self.type_activite.choices.append((str(type.id), type.nom))
        self.type_activite.default = str(activity.type_activite.id)
        self.process()

    def edit(self, activity:Activite):
        type = get_activity_type_by_id(int(self.type_activite.data))
        if type:
            activity.nom = self.nom.data
            activity.description = self.description.data
            activity.max_clients = self.max_clients.data
            activity.type_activite = type
            db.session.commit()