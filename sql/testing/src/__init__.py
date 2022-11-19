from core.database import db, Base, session
from modeles.client import Client
from modeles.poney import Poney
from datetime import datetime
from modeles import modeles

def choices(session):
    print("Choisissez une option :")
    print("1 - Créer un client")
    print("2 - Créer un poney")
    print("3 - Créer un moniteur")
    print("4 - Créer une sortie")

    choice = int(input("Votre réponse : "))

    if choice == 1:
        create_client(session)
    elif choice == 2:
        create_poney(session)

def create_client(session):
    session.add(Client(
        email=input("Email : "), 
        mdp=input("Mot de passe : "),
        prenom=input("Prenom : "),
        nom=input("Nom : "),
        tel=input("Telephone (ex: 06XXXXXXXX) : "),
        addr=input("Addresse : "),
        date_cotisation=datetime.utcnow()
    ))
    session.commit()

def create_poney(session):
    session.add(Poney(
        nom=input("Nom : "),
        charge_max=int(input("Charge maximale (g) : ")),
        date_naissance=datetime.utcnow(),
        taille=int(input("Taille (cm) : "))
    ))
    session.commit()

if __name__ == "__main__":
    Base.metadata.create_all(db)
    # act = session.query(Activite).first()
    # print(act.type_activite.id)
    choices(session)
    session.close()