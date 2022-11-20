CREATE TABLE CLIENTS(
    IdC int unsigned primary key not null auto_increment,
    EmailC varchar(255),
    MotDePasseC varchar(255),
    PrenomC varchar(50) not null,
    NomC varchar(200) not null,
    TelephoneC varchar(13) not null,
    AddresseC varchar(255) not null,
    DateCotisation date 
);

CREATE TABLE MONITEURS(
    IdM int unsigned primary key not null auto_increment,
    PrenomM varchar(50) not null,
    NomM varchar(200) not null,
    TelephoneM varchar(13) not null
);

CREATE TABLE PONEYS(
    IdP int unsigned primary key not null auto_increment,
    NomP varchar(200) not null,
    ChargeMax int unsigned not null, -- en grammes
    dateNaissanceP date not null,
    tailleP smallint unsigned not null, -- taille en cm
    imgP longblob
);

CREATE TABLE TYPESACTIVITE(
    IdTa int unsigned primary key not null auto_increment,
    NomTa varchar(50) not null
);

CREATE TABLE ACTIVITES(
    IdA int unsigned primary key not null auto_increment,
    NomA varchar(50) not null,
    DescriptionA varchar(255),
    IdTa int unsigned not null,
    MaxClients tinyint unsigned not null check(MaxClients > 0 and MaxClients < 11),
    CONSTRAINT fk_activites_typesactivite FOREIGN KEY (IdTa) REFERENCES TYPESACTIVITE(IdTa)
);

CREATE TABLE SORTIES(
    IdS int unsigned primary key auto_increment,
    IdA int unsigned not null,
    DateSortie datetime not null,
    DureeSortie int not null, -- duree en minutes
    CONSTRAINT fk_sorties_activites FOREIGN KEY (IdA) REFERENCES ACTIVITES(IdA)
);

CREATE TABLE ENCADRER(
    IdM int unsigned,
    IdS int unsigned,
    CONSTRAINT fk_encadrer_sorties FOREIGN KEY (IdS) REFERENCES SORTIES(IdS),
    CONSTRAINT fk_encadrer_moniteurs FOREIGN KEY (IdM) REFERENCES MONITEURS(IdM),
    primary key (IdM, IdS)
);

CREATE TABLE MONTER(
    IdS int unsigned not null,
    IdC int unsigned not null,
    IdP int unsigned not null,
    CONSTRAINT fk_monter_sorties FOREIGN KEY (IdS) REFERENCES SORTIES(IdS),
    CONSTRAINT fk_monter_clients FOREIGN KEY (IdC) REFERENCES CLIENTS(IdC),
    CONSTRAINT fk_monter_poneys FOREIGN KEY (IdP) REFERENCES PONEYS(IdP),
    primary key (IdS, IdC, IdP)
);

-- TRIGGER --

delimiter |

CREATE or REPLACE trigger repos_poney_I before insert on MONTER for each row
begin
    declare mes varchar(100);
    declare last_sortie datetime;
    declare new_sortie datetime;
    select max(DateSortie) into last_sortie from SORTIES natural join MONTER where IdP = new.IdP;
    select max(DateSortie) into new_sortie from SORTIES natural join MONTER where IdP = new.IdP and SORTIES.IdS = new.IdS;
    if TIMESTAMPDIFF(hour, last_sortie, new_sortie) < 1 then
        set mes = concat ('Le poney a besoin de plus de repos');
        signal SQLSTATE '45000' set MESSAGE_TEXT = mes;
    end if;
end |

CREATE or REPLACE trigger repos_poney_U before update on MONTER for each row
begin
    declare mes varchar(100);
    declare last_sortie datetime;
    declare new_sortie datetime;
    select max(DateSortie) into last_sortie from SORTIES natural join MONTER where IdP = new.IdP;
    select max(DateSortie) into new_sortie from SORTIES natural join MONTER where IdP = new.IdP and SORTIES.IdS = new.IdS;
    if TIMESTAMPDIFF(hour, last_sortie, new_sortie) < 1 then
        set mes = concat ('Le poney a besoin de plus de repos');
        signal SQLSTATE '45000' set MESSAGE_TEXT = mes;
    end if;
end |

CREATE or REPLACE trigger max_client_sortie before insert on MONTER for each row
begin
  declare max_client int;
  declare id_activite int;
  declare nb_clients int;
  declare mes varchar(100);
  select MaxClients into max_client from ACTIVITES natural join SORTIES where IdS = new.IdS;
  select IdA into id_activite from ACTIVITES natural join SORTIES where IdS = new.IdS;
  select count(IdC) into nb_clients from MONTER natural join SORTIES where IdA = id_activite;
  if max_client < nb_clients then
    set mes = concat('Trop de personne inscrite pour cette activite');
    signal SQLSTATE '45000' set MESSAGE_TEXT = mes;
  end if;
end |

CREATE or REPLACE trigger check_cotisation before insert on MONTER for each row
begin
  declare date_now date;
  declare date_cotisation date;
  declare mes varchar(100);
  set date_now = CURDATE();
  select DateCotisation into date_cotisation from CLIENTS natural join MONTER where MONTER.IdC = new.IdC;
  if TIMESTAMPDIFF(year, date_cotisation, date_now) > 1 then
    set mes = concat('Problème de cotisation');
    signal SQLSTATE '45000' set MESSAGE_TEXT = mes;
  end if;
end |

delimiter ;