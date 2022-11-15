from core.database import Base
from sqlalchemy import Column, Integer, String

class TypeActivite(Base):
    __tablename__ = "TYPESACTIVITE"

    id = Column("idTa", Integer, primary_key=True, autoincrement=True)
    nom = Column("NomTa", String(50), nullable=False)