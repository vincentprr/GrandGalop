from ..core.database import db
from sqlalchemy.dialects.mysql import INTEGER

class Monter(db.Model):
    __tablename__ = "MONTER"

    id_sortie = db.Column("IdS", INTEGER(unsigned=True), db.ForeignKey("SORTIES.IdS"), primary_key=True, nullable=True)
    sortie = db.relationship("Sortie", backref="monter")
    id_client = db.Column("IdC", INTEGER(unsigned=True), db.ForeignKey("CLIENTS.IdP"), primary_key=True, nullable=True)
    client = db.relationship("Client", backref="monter")
    id_poney = db.Column("IdP", INTEGER(unsigned=True), db.ForeignKey("PONEYS.IdP"), primary_key=True, nullable=True)
    poney = db.relationship("Poney", backref="monter")