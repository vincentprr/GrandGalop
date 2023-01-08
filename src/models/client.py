from ..core.database import db
from sqlalchemy.orm import backref
from sqlalchemy import Date
from sqlalchemy.dialects.mysql import INTEGER

class Client(db.Model):
    __tablename__ = "CLIENTS"

    id = db.Column("IdP", INTEGER(unsigned=True), db.ForeignKey("PERSONNES.IdP"), primary_key=True, autoincrement=True)
    date_cotisation = db.Column("DateCotisation", Date)
    personne = db.relationship("Personne", uselist=False, backref=backref("client", uselist=False))