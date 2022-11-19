from core.database import Base
from sqlalchemy import Column, String
from sqlalchemy.dialects.mysql import INTEGER
from core.constant import STRING_MIDLE_SIZE, STRING_LITTLE_SIZE, STRING_TEL_SIZE

class Moniteur(Base):
    __tablename__ = "MONITEURS"

    id = Column("IdM", INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    prenom = Column("PrenomM", String(STRING_LITTLE_SIZE), nullable=False)
    nom = Column("NomM", String(STRING_MIDLE_SIZE), nullable=False)
    tel = Column("TelephoneC", String(STRING_TEL_SIZE), nullable=False)