from ..core.database import db
from ..models.poney import Poney

def get_poneys(**kwargs) -> "list[Poney]":
    return Poney.query.filter_by(**kwargs).all()