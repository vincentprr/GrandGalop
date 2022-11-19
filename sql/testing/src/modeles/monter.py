from core.database import Base
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import INTEGER

class Monter(Base):
    __tablename__ = "MONTER"

    id_sortie = Column("IdS", INTEGER(unsigned=True), ForeignKey("SORTIES.IdS"), primary_key=True, nullable=True)
    activite = relationship("Sortie")
    id_client = Column("IdC", INTEGER(unsigned=True), ForeignKey("CLIENTS.IdC"), primary_key=True, nullable=True)
    client = relationship("Client")
    id_poney = Column("IdP", INTEGER(unsigned=True), ForeignKey("PONEYS.IdP"), primary_key=True, nullable=True)
    poney = relationship("Poney")