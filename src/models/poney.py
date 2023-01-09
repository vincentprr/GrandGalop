from ..core.database import db
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.dialects.mysql import LONGBLOB, INTEGER
from ..core.constant import STRING_MIDLE_SIZE

class Poney(db.Model):
    __tablename__ = "PONEYS"

    id = Column("IdP", INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    nom = Column("NomP", String(STRING_MIDLE_SIZE), nullable=False)
    charge_max = Column("ChargeMax", INTEGER(unsigned=True), nullable=False)
    date_naissance = Column("dateNaissanceP", Date, nullable=False)
    taille = Column("tailleP", Integer, nullable=False)
    img = Column("imgP", LONGBLOB)