from core.database import Base
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import INTEGER

class Encadrer(Base):
    __tablename__ = "ENCADRER"

    id_moniteur = Column("IdM", INTEGER(unsigned=True), ForeignKey("MONITEURS.IdM"), primary_key=True, nullable=True)
    id_sortie = Column("IdS", INTEGER(unsigned=True), ForeignKey("SORTIES.IdS"), primary_key=True, nullable=True)