from core.database import Base
from sqlalchemy import Column, Integer, String, Date

class Client(Base):
    __tablename__ = "CLIENTS"

    id = Column("IdC", Integer, primary_key=True, autoincrement=True)
    email = Column("EmailC", String(255), nullable=False)
    mdp = Column("MotDePasseC", String(255), nullable=False)
    prenom = Column("PrenomC", String(50), nullable=False)
    nom = Column("NomC", String(200), nullable=False)
    tel = Column("TelephoneC", String(13), nullable=False)
    addr = Column("AddresseC", String(255), nullable=False)
    date_cotisation = Column("DateCotisation", Date)