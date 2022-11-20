from core.database import Base
from sqlalchemy import Column, ForeignKey, Table
from sqlalchemy.dialects.mysql import INTEGER

Encadrer = Table(
    "ENCADRER",
    Base.metadata,
    Column("IdS", INTEGER(unsigned=True), ForeignKey("SORTIES.IdS"), nullable=True),
    Column("IdM", INTEGER(unsigned=True), ForeignKey("MONITEURS.IdM"), nullable=True)
)