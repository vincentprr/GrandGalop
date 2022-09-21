DROP TABLE IF EXISTS MONTER, SORTIES, ACTIVITES, TYPESACTIVITE, PONEYS, MONITEURS, CLIENTS;

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
    DescriptionA varchar(255),
    IdTa int not null,
    MaxClients int not null check(MaxClients > 0 and MaxClients < 11),
    CONSTRAINT fk_activites_typesactivite FOREIGN KEY (IdTa) REFERENCES TYPESACTIVITE(IdTa)
);

CREATE TABLE SORTIES(
    IdS int primary key,
    IdA int not null,
    IdM int not null,
    DateSortie datetime not null,
    CONSTRAINT fk_sorties_activites FOREIGN KEY (IdA) REFERENCES ACTIVITES(IdA),
    CONSTRAINT fk_sorties_moniteurs FOREIGN KEY (IdM) REFERENCES MONITEURS(IdM)
);

CREATE TABLE MONTER(
    IdS int not null,
    IdC int not null,
    IdP int not null,
    CONSTRAINT fk_monter_sorties FOREIGN KEY (IdS) REFERENCES SORTIES(IdS),
    CONSTRAINT fk_monter_clients FOREIGN KEY (IdC) REFERENCES CLIENTS(IdC),
    CONSTRAINT fk_monter_poneys FOREIGN KEY (IdP) REFERENCES PONEYS(IdP)
);