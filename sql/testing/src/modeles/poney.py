from core.database import Base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.dialects.mysql import LONGBLOB

class Poney(Base):
    __tablename__ = "PONEYS"

    id = Column("IdP", Integer, primary_key=True, autoincrement=True)
    nom = Column("NomP", String(200), nullable=False)
    charge_max = Column("ChargeMax", Integer, nullable=False)
    date_naissance = Column("dateNaissanceP", Date, nullable=False)
    taille = Column("tailleP", Integer, nullable=False)
    img = Column("imgP", LONGBLOB)