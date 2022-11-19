from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from .constant import DATABASE_USER, DATABASE_IP, DATABASE_PASSWORD, DATBASE_NAME

def create_connection():
    """
    ouverture d'une connexion MySQL
    paramètres:
       user     (str) le login MySQL de l'utilsateur
       passwd   (str) le mot de passe MySQL de l'utilisateur
       host     (str) le nom ou l'adresse IP de la machine hébergeant le serveur MySQL
       database (str) le nom de la base de données à utiliser
    résultat: l'objet qui gère le connection MySQL si tout s'est bien passé
    """
    try:
        #creation de l'objet gérant les interactions avec le serveur de BD
        cnx = create_engine('mysql://'+ DATABASE_USER +':'+ DATABASE_PASSWORD +'@'+ DATABASE_IP +'/'+ DATBASE_NAME)
    except Exception as err:
        print(err)
        raise err
    return cnx

db = create_connection()
session = sessionmaker()(bind=db)
Base = declarative_base()