insert into CLIENTS (EmailC, MotDePasseC, PrenomC, NomC, TelephoneC, AddresseC, DateCotisation) values 
('exemple@gmail.com', 'hdgSFJH<S315S<D4F', 'Jean', 'Dupont', '0612554720', '333 rue du diable Orleans', '2021-09-13'),
('anothermail@yahoo.com', 'uidgu455', 'Pierre', 'Dupond', '0612359557', '666 rue du paradie Orleans', '2020-05-01'),
('plusdidee@mail.com', 'jjwshrg564s<6', 'Jonhy', 'Joestar', '0732564752', '45 rue du cheval Ariba', '2021-06-15'),
('cragraddonnauve-4408@yopmail.com', 'rd<g16qtrg4', 'Fugo', 'Panacotta', '0221358457', "20 rue d'Italie Paris", '2020-12-25'),
('freijeubujawu-5861@yopmail.com', '53d4gt654z', 'Gyro', 'Zeppeli', '0321545795', '1400 rue haute Lille', '2021-10-23');

insert into MONITEURS (PrenomM, NomM, TelephoneM) values
('Bartolemu', 'Kuma', '0621326545'),
('Poco', 'Loco', '0512326548');

insert into PONEYS (NomP, ChargeMax, dateNaissanceP, tailleP, imgP) values
('Silver Bullet', 70, '2017-03-27', 123, null),
('Hey! Ya!', 60, '2016-05-19', 150, null),
('Valkyrie', 90, '2017-01-01', 163, null);

insert into TYPESACTIVITE (NomTa) values
("Balade"),
("cours"),
("initiation");

insert into ACTIVITES (NomA, DescriptionA, IdTa, MaxClients) values
("Balade en foret", "petite en foret pour tout les ages", 1, 10),
("cours de saut", "apprendre à faire des sout à cheval", 2, 5),
("premiere fois", "initiation à l'équitation pour les débutants", 3, 6);

insert into SORTIES (IdA, IdM, DateSortie) values
(1, 2, '2022-11-10 10:30:01'),
(2, 1, '2022-12-11 14:00:00'),
(3, 1, '2023-03-20 09:15:00');

insert into MONTER (IdS, IdC, IdP) values
(1, 1, 3),
(1, 2, 2),
(2, 3, 1),
(2, 5, 3),
(3, 4, 1);