from ..core.database import db
from sqlalchemy import Column, String
from sqlalchemy.dialects.mysql import INTEGER
from ..core.constant import STRING_LITTLE_SIZE

class TypeActivite(db.Model):
    __tablename__ = "TYPESACTIVITE"

    id = Column("IdTa", INTEGER(unsigned=True), primary_key=True)
    nom = Column("NomTa", String(STRING_LITTLE_SIZE), nullable=False)