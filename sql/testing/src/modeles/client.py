from core.database import db, Base
from sqlalchemy import Column, Integer, String, Date

class Client(Base):
    __tablename__ = "CLIENTS"

    id = Column("IdC", Integer, primary_key=True, autoincrement=True)
    email = Column("EmailC", String(255))
    mdp = Column("MotDePasseC", String(255))
    prenom = Column("PrenomC", String(50))
    nom = Column("NomC", String(200))
    tel = Column("TelephoneC", String(13))
    addr = Column("AddresseC", String(255))
    date_cotisation = Column("DateCotisation", Date)