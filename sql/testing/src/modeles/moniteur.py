from core.database import Base
from sqlalchemy import Column, Integer, String

class Moniteur(Base):
    __tablename__ = "MONITEURS"

    id = Column("IdM", Integer, primary_key=True, autoincrement=True)
    prenom = Column("PrenomM", String(50), nullable=False)
    nom = Column("NomM", String(200), nullable=False)
    tel = Column("TelephoneC", String(13), nullable=False)