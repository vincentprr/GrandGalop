from core.database import db, Base, session

from modeles.client import Client
from modeles.poney import Poney
from modeles.moniteur import Moniteur
from modeles.type_activite import TypeActivite
from modeles.activite import Activite
from modeles.sortie import Sortie
from modeles.monter import Monter

from datetime import datetime
from modeles import modeles

def choices(session):
    print("Choisissez une option :")
    print("1 - Créer un client")
    print("2 - Créer un poney")
    print("3 - Créer un moniteur")
    print("4 - Créer un type d'activité")
    print("5 - Créer une activité")
    print("6 - Créer une sortie")
    print("7 - Planifier monter un poney durant une sortie")

    choice = int(input("Votre réponse : "))

    if choice == 1:
        create_client(session)
    elif choice == 2:
        create_poney(session)
    elif choice == 3:
        create_moniteur(session)
    elif choice == 4:
        create_type_activite(session)
    elif choice == 5:
        create_activite(session)
    elif choice == 6:
        create_sortie(session)
    elif choice == 7:
        create_monter(session)

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

def create_moniteur(session):
    session.add(Moniteur(
        prenom=input("Prenom : "),
        nom=input("Nom : "),
        tel=input("Telephone (ex: 06XXXXXXXX) : ")
    ))
    session.commit()

def create_type_activite(session):
    session.add(TypeActivite(
        nom=input("Nom : ")
    ))
    session.commit()

def create_activite(session):
    nom=input("Nom : ")
    description=input("Description : ")
    max_clients=int(input("Maximum de clients : "))

    types_act = session.query(TypeActivite).all()
    if len(types_act) > 0:
        print("-- Type d'activité --")
        for type_act in types_act:
            print(str(type_act.id) +" - "+ type_act.nom)
        
        id_type_act = int(input("Votre choix : "))

        if session.query(TypeActivite).filter(TypeActivite.id == id_type_act).first() != None:
            session.add(Activite(
                nom=nom,
                description=description,
                max_clients=max_clients,
                id_type_activite=id_type_act
            ))
            session.commit()
        else:
            print("Le type sélectionner n'existe pas...")
    else:
        print("Il n'y a aucun type d'activité...")

def create_sortie(session):
    activites = session.query(Activite).all()
    if len(activites) > 0:
        print("-- Activité --")
        for activite in activites:
            print(str(activite.id) +" - "+ activite.nom)

        id_activite = int(input("Votre choix : "))

        if session.query(Activite).filter(Activite.id == id_activite).first() != None:
            moniteurs = session.query(Moniteur).all()

            if len(moniteurs) > 0:
                print("-- Moniteur --")
                for moniteur in moniteurs:
                    print(str(moniteur.id) +" - "+ moniteur.nom +" "+ moniteur.prenom)
                
                id_moniteur= int(input("Votre choix : "))

                if session.query(Moniteur).filter(Moniteur.id == id_moniteur).first() != None:
                    session.add(Sortie(
                        id_activite=id_activite,
                        id_moniteur=id_moniteur,
                        date_sortie=datetime.utcnow()
                    ))
                    session.commit()
                else:
                    print("Le moniteur sélectionné n'existe pas...")
            else:
                print("Il n'y a aucun moniteurs...")
        else:
            print("L'activité sélectionner n'existe pas...")
    else:
        print("Il n'y a aucune activité de proposer...")

def create_monter(session):
    sorties = session.query(Sortie).all()
    if len(sorties) > 0:
        print("-- Sortie --")
        for sortie in sorties:
            print(str(sortie.id) +" - "+ sortie.activite.nom +" - "+ str(sortie.date_sortie))
        
        id_sortie = int(input("Votre choix : "))

        if session.query(Sortie).filter(Sortie.id == id_sortie).first() != None:
            clients = session.query(Client).all()

            if len(clients) > 0:
                print("-- Client --")
                for client in clients:
                    print(str(client.id) +" - "+ client.nom +" "+ client.prenom)
                
                id_client= int(input("Votre choix : "))

                if session.query(Client).filter(Client.id == id_client).first() != None:
                    poneys = session.query(Poney).all()

                    if len(poneys) > 0:
                        print("-- Poney --")
                        for poney in poneys:
                            print(str(poney.id) +" - "+ poney.nom)

                        id_poney = int(input("Votre choix : "))

                        if session.query(Poney).filter(Poney.id == id_poney).first() != None:
                            session.add(Monter(
                                id_sortie = id_sortie,
                                id_client = id_client,
                                id_poney = id_poney
                            ))
                            session.commit()
                        else:
                            print("Le poney sélectionné n'existe pas...")
                    else:
                        print("Il n'y aucun poneys...")
                else:
                    print("Le client sélectionné n'existe pas...")
            else:
                print("Il n'y a aucun clients...")
        else:
            print("La sortie sélectionnée existe pas...")
    else:
        print("Il n'y a aucune sorties de planifié...")

if __name__ == "__main__":
    Base.metadata.create_all(db)
    # act = session.query(Activite).first()
    # print(act.type_activite.id)
    choices(session)
    session.close()