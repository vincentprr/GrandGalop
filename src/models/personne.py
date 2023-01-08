from ..core.database import db
from sqlalchemy import String, Date
from sqlalchemy.dialects.mysql import INTEGER, TEXT
from flask_login import UserMixin
from ..core.constant import STRING_MAX_SIZE, STRING_TEL_SIZE, STRING_MIDLE_SIZE, STRING_LITTLE_SIZE

class Personne(db.Model, UserMixin):
    __tablename__ = "PERSONNES"

    id = db.Column("IdP", INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    email = db.Column("EmailC", String(STRING_MAX_SIZE), nullable=False)
    mdp = db.Column("MotDePasseC", TEXT, nullable=False)
    prenom = db.Column("PrenomC", TEXT, nullable=False)
    nom = db.Column("NomC", TEXT, nullable=False)
    tel = db.Column("TelephoneC", String(STRING_TEL_SIZE), nullable=False)
    adr = db.Column("AdresseC", TEXT, nullable=False)

    def get_id(self):
        return self.id