from ..core.database import db
from sqlalchemy import Column, String
from sqlalchemy.dialects.mysql import INTEGER, TINYINT
from ..core.constant import STRING_LITTLE_SIZE, STRING_MAX_SIZE
from sqlalchemy.orm import backref

class Activite(db.Model):
    __tablename__ = "ACTIVITES"

    id = Column("IdA", INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    nom = Column("NomA", String(STRING_LITTLE_SIZE), nullable=False)
    description = Column("DescriptionA", String(STRING_MAX_SIZE), nullable=False)
    max_clients = Column("MaxClients", TINYINT(unsigned=True), nullable=False)
    id_type_activite = Column("IdTa", INTEGER(unsigned=True), db.ForeignKey("TYPESACTIVITE.IdTa"), nullable=True)
    type_activite = db.relationship("TypeActivite", uselist=False, backref="activites")