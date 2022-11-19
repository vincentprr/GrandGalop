from core.database import Base
from sqlalchemy import Column, String, Date
from sqlalchemy.dialects.mysql import INTEGER
from core.constant import STRING_MAX_SIZE, STRING_TEL_SIZE, STRING_MIDLE_SIZE, STRING_LITTLE_SIZE

class Client(Base):
    __tablename__ = "CLIENTS"

    id = Column("IdC", INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    email = Column("EmailC", String(STRING_MAX_SIZE), nullable=False)
    mdp = Column("MotDePasseC", String(STRING_MAX_SIZE), nullable=False)
    prenom = Column("PrenomC", String(STRING_LITTLE_SIZE), nullable=False)
    nom = Column("NomC", String(STRING_MIDLE_SIZE), nullable=False)
    tel = Column("TelephoneC", String(STRING_TEL_SIZE), nullable=False)
    addr = Column("AddresseC", String(STRING_MAX_SIZE), nullable=False)
    date_cotisation = Column("DateCotisation", Date)