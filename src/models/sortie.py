from ..core.database import db
from sqlalchemy import DateTime, ForeignKey
from sqlalchemy.dialects.mysql import INTEGER

class Sortie(db.Model):
    __tablename__ = "SORTIES"

    id = db.Column("IdS", INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    id_activite = db.Column("IdA", INTEGER(unsigned=True), ForeignKey("ACTIVITES.IdA"), nullable=True)
    activite = db.relationship("Activite", uselist=False)
    date = db.Column("DateSortie", DateTime, nullable=False)
    duree = db.Column("DureeSortie", INTEGER(unsigned=True), nullable=False)
    moniteurs = db.relationship("Moniteur", secondary='ENCADRER', backref="sorties")