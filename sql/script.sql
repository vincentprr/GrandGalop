DROP TABLE IF EXISTS CLIENTS, MONITEURS, ACTIVITES, TYPESACTIVITE, PONEYS CASCADE CONSTRAINTS;

CREATE TABLE CLIENTS(
    IdC int primary key not null auto_increment,
    EmailC varchar(255),
    MotDePasseC varchar(255),
    PrenomC varchar(50) not null,
    NomC varchar(200) not null,
    TelephoneC varchar(13) not null,
    AddresseC varchar(255) not null,
    DateCotisation date 
);

CREATE TABLE MONITEURS(
    IdM int primary key not null auto_increment,
    PrenomM varchar(50) not null,
    NomM varchar(200) not null,
    TelephoneM varchar(13) not null
);

CREATE TABLE PONEYS(
    IdP int primary key not null auto_increment,
    NomP varchar(200) not null,
    ChargeMax int not null,
    dateNaissanceP date not null,
    tailleP int not null, -- taille en cm
    imgP longblob
);

CREATE TABLE TYPESACTIVITE(
    IdTa int primary key not null auto_increment,
    NomTa varchar(50) not null
);

CREATE TABLE ACTIVITES(
    IdA int primary key not null auto_increment,
    NomA varchar(50) not null,
    IdTa int not null,
    CONSTRAINT fk_activites_typesactivite FOREIGN KEY (IdTa) REFERENCES TYPESACTIVITE(IdTa)
);

CREATE TABLE SORTIES(
    IdA int not null,
    DateSortie date not null,
    IdM int not null,
    CONSTRAINT fk_sorties_activites FOREIGN KEY (IdA) REFERENCES ACTIVITES(IdA),
    CONSTRAINT fk_sorties_moniteurs FOREIGN KEY (IdM) REFERENCES MONITEURS(IdM)
);