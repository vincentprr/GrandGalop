from core.database import db, Base
from modeles import modeles

if __name__ == "__main__":
    Base.metadata.create_all(db)
    db.close()