from core.database import Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import INTEGER, TINYINT
from core.constant import STRING_LITTLE_SIZE, STRING_MAX_SIZE

class Activite(Base):
    __tablename__ = "ACTIVITES"

    id = Column("IdA", INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    nom = Column("NomA", String(STRING_LITTLE_SIZE), nullable=False)
    description = Column("DescriptionA", String(STRING_MAX_SIZE), nullable=False)
    max_clients = Column("MaxClients", TINYINT(unsigned=True), nullable=False)
    id_type_activite = Column("IdTa", INTEGER(unsigned=True), ForeignKey("TYPESACTIVITE.IdTa"), nullable=True)
    type_activite = relationship("TypeActivite")