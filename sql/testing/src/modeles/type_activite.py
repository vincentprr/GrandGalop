from core.database import Base
from sqlalchemy import Column, String
from sqlalchemy.dialects.mysql import INTEGER
from core.constant import STRING_LITTLE_SIZE

class TypeActivite(Base):
    __tablename__ = "TYPESACTIVITE"

    id = Column("IdTa", INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    nom = Column("NomTa", String(STRING_LITTLE_SIZE), nullable=False)