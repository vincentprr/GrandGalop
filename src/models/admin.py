from ..core.database import db
from sqlalchemy.dialects.mysql import INTEGER, LONGBLOB
from sqlalchemy.orm import backref

class Admin(db.Model):
    __tablename__ = "ADMINS"

    id = db.Column("IdP", INTEGER(unsigned=True), db.ForeignKey("PERSONNES.IdP"), primary_key=True, autoincrement=True)
    image = db.Column("Image", LONGBLOB)
    personne = db.relationship("Personne", uselist=False, backref=backref("admin", uselist=False))
    