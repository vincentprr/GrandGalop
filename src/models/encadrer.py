from ..core.database import db
from sqlalchemy.dialects.mysql import INTEGER

class Encadrer(db.Model):
    __tablename__ = "ENCADRER"

    id_moniteur = db.Column("IdM", INTEGER(unsigned=True), db.ForeignKey("MONITEURS.IdP"), primary_key=True)
    id_sortie = db.Column("IdS", INTEGER(unsigned=True), db.ForeignKey("SORTIES.IdS"), primary_key=True)