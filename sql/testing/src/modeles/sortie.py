from core.database import Base
from sqlalchemy import Column, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import INTEGER
from .encadrer import Encadrer

class Sortie(Base):
    __tablename__ = "SORTIES"

    id = Column("IdS", INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    id_activite = Column("IdA", INTEGER(unsigned=True), ForeignKey("ACTIVITES.IdA"), nullable=True)
    activite = relationship("Activite")
    date_sortie = Column("DateSortie", DateTime, nullable=False)
    duree_sortie = Column("DureeSortie", INTEGER(unsigned=True), nullable=False)
    moniteurs = relationship("Moniteur", secondary=Encadrer)