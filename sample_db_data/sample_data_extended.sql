-- Pasul 1: Stergere date existente
DELETE FROM grupe_utilizator;
DELETE FROM programari_examen;
DELETE FROM materii;
DELETE FROM grupe;
DELETE FROM specializari;
DELETE FROM facultati;
DELETE FROM utilizator;

-- Pasul 2: Introducere date de test
-- 1. Inserare Facultăți
INSERT INTO facultati (id, nume)
VALUES
  (NEWID(), 'Facultatea de Matematica si Informatica'),
  (NEWID(), 'Facultatea de Litere'),
  (NEWID(), 'Facultatea de Inginerie'),
  (NEWID(), 'Facultatea de Stiinte Economice'),
  (NEWID(), 'Facultatea de Fizica'),
  (NEWID(), 'Facultatea de Chimie'),
  (NEWID(), 'Facultatea de Biologie'),
  (NEWID(), 'Facultatea de Medicina'),
  (NEWID(), 'Facultatea de Drept'),
  (NEWID(), 'Facultatea de Arte'),
  (NEWID(), 'Facultatea de Teologie'),
  (NEWID(), 'Facultatea de Filosofie'),
  (NEWID(), 'Facultatea de Geografie'),
  (NEWID(), 'Facultatea de Psihologie'),
  (NEWID(), 'Facultatea de Sociologie'),
  (NEWID(), 'Facultatea de Inginerie Civila'),
  (NEWID(), 'Facultatea de Agricultura'),
  (NEWID(), 'Facultatea de Stiinte ale Naturii'),
  (NEWID(), 'Facultatea de Informatica'),
  (NEWID(), 'Facultatea de Management');

-- 2. Inserare Specializări
INSERT INTO specializari (id, id_facultate, nume)
VALUES
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Matematica si Informatica'), 'Informatica'),
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Litere'), 'Filologie'),
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Inginerie'), 'Automatica si Calculatoare'),
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Stiinte Economice'), 'Contabilitate'),
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Fizica'), 'Fizica Aplicata'),
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Chimie'), 'Chimie Generala'),
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Biologie'), 'Biologie Moleculara'),
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Medicina'), 'Medicina Generala'),
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Drept'), 'Drept Penal'),
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Arte'), 'Arte Plastice'),
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Teologie'), 'Teologie Ortodoxa'),
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Filosofie'), 'Filosofie Contemporana'),
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Geografie'), 'Geografie Fizica'),
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Psihologie'), 'Psihologie Clinica'),
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Sociologie'), 'Sociologie Urbana'),
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Inginerie Civila'), 'Constructii Civile'),
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Agricultura'), 'Agricultura Durabila'),
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Stiinte ale Naturii'), 'Ecologie'),
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Informatica'), 'Tehnologia Informatiei'),
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Management'), 'Management Strategic');

-- 3. Inserare Grupe
INSERT INTO grupe (id, id_facultate, id_specializare, an, numar_grupa, litera_semigrupa)
VALUES
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Matematica si Informatica'), (SELECT id FROM specializari WHERE nume = 'Informatica'), 1, 101, 1),
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Litere'), (SELECT id FROM specializari WHERE nume = 'Filologie'), 1, 102, 2),
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Inginerie'), (SELECT id FROM specializari WHERE nume = 'Automatica si Calculatoare'), 2, 103, 1),
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Stiinte Economice'), (SELECT id FROM specializari WHERE nume = 'Contabilitate'), 2, 104, 2),
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Fizica'), (SELECT id FROM specializari WHERE nume = 'Fizica Aplicata'), 1, 105, 1),
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Chimie'), (SELECT id FROM specializari WHERE nume = 'Chimie Generala'), 2, 106, 1),
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Biologie'), (SELECT id FROM specializari WHERE nume = 'Biologie Moleculara'), 3, 107, 2),
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Medicina'), (SELECT id FROM specializari WHERE nume = 'Medicina Generala'), 4, 108, 1),
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Drept'), (SELECT id FROM specializari WHERE nume = 'Drept Penal'), 1, 109, 2),
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Arte'), (SELECT id FROM specializari WHERE nume = 'Arte Plastice'), 2, 110, 1),
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Teologie'), (SELECT id FROM specializari WHERE nume = 'Teologie Ortodoxa'), 3, 111, 2),
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Filosofie'), (SELECT id FROM specializari WHERE nume = 'Filosofie Contemporana'), 4, 112, 1),
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Geografie'), (SELECT id FROM specializari WHERE nume = 'Geografie Fizica'), 1, 113, 2),
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Psihologie'), (SELECT id FROM specializari WHERE nume = 'Psihologie Clinica'), 1, 114, 1),
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Sociologie'), (SELECT id FROM specializari WHERE nume = 'Sociologie Urbana'), 2, 115, 2),
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Inginerie Civila'), (SELECT id FROM specializari WHERE nume = 'Constructii Civile'), 3, 116, 1),
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Agricultura'), (SELECT id FROM specializari WHERE nume = 'Agricultura Durabila'), 4, 117, 2),
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Stiinte ale Naturii'), (SELECT id FROM specializari WHERE nume = 'Ecologie'), 1, 118, 1),
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Informatica'), (SELECT id FROM specializari WHERE nume = 'Tehnologia Informatiei'), 2, 119, 2),
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Management'), (SELECT id FROM specializari WHERE nume = 'Management Strategic'), 3, 120, 1);

-- 4. Inserare Utilizatori (Profesori, Studenti)
INSERT INTO utilizator (id, first_name, last_name, email, password, rol)
VALUES
  (NEWID(), 'Ion', 'Popescu', 'ion.popescu@univ.com', 'parola123', 'PROFESSOR'),
  (NEWID(), 'Maria', 'Ionescu', 'maria.ionescu@univ.com', 'parola123', 'STUDENT'),
  (NEWID(), 'Alex', 'Vasile', 'alex.vasile@univ.com', 'parola123', 'STUDENT'),
  (NEWID(), 'Ana', 'Georgescu', 'ana.georgescu@univ.com', 'parola123', 'PROFESSOR'),
  (NEWID(), 'Ioana', 'Popa', 'ioana.popa@univ.com', 'parola123', 'PROFESSOR'),
  (NEWID(), 'Mihai', 'Ionescu', 'mihai.ionescu@univ.com', 'parola123', 'STUDENT'),
  (NEWID(), 'Elena', 'Radu', 'elena.radu@univ.com', 'parola123', 'STUDENT'),
  (NEWID(), 'Vasile', 'Luca', 'vasile.luca@univ.com', 'parola123', 'PROFESSOR'),
  (NEWID(), 'Gheorghe', 'Mihaila', 'gheorghe.mihaila@univ.com', 'parola123', 'STUDENT'),
  (NEWID(), 'Andrei', 'Cojocaru', 'andrei.cojocaru@univ.com', 'parola123', 'PROFESSOR'),
  (NEWID(), 'Sofia', 'Rusu', 'sofia.rusu@univ.com', 'parola123', 'STUDENT'),
  (NEWID(), 'Marius', 'Dima', 'marius.dima@univ.com', 'parola123', 'STUDENT'),
  (NEWID(), 'Adriana', 'Tudor', 'adriana.tudor@univ.com', 'parola123', 'PROFESSOR'),
  (NEWID(), 'Doru', 'Bucur', 'doru.bucur@univ.com', 'parola123', 'STUDENT'),
  (NEWID(), 'Daniela', 'Sava', 'daniela.sava@univ.com', 'parola123', 'STUDENT'),
  (NEWID(), 'Gabriel', 'Munteanu', 'gabriel.munteanu@univ.com', 'parola123', 'PROFESSOR'),
  (NEWID(), 'Lucia', 'Vasilescu', 'lucia.vasilescu@univ.com', 'parola123', 'STUDENT'),
  (NEWID(), 'Loredana', 'Stanescu', 'loredana.stanescu@univ.com', 'parola123', 'STUDENT'),
  (NEWID(), 'Radu', 'Ciobanu', 'radu.ciobanu@univ.com', 'parola123', 'PROFESSOR'),
  (NEWID(), 'Costel', 'Iordache', 'costel.iordache@univ.com', 'parola123', 'STUDENT');

-- 5. Inserare Materii (corectat pentru nume_abreviat)
INSERT INTO materii (id, id_grupa, id_profesor, semestrul, nume, nume_abreviat, numar_credite, durata_examen_minute)
VALUES
  (NEWID(), (SELECT id FROM grupe WHERE numar_grupa = 101), (SELECT id FROM utilizator WHERE email = 'ion.popescu@univ.com'), 1, 'Matematica Discreta', 'MathDiscr', 6, 120),
  (NEWID(), (SELECT id FROM grupe WHERE numar_grupa = 102), (SELECT id FROM utilizator WHERE email = 'ana.georgescu@univ.com'), 1, 'Literatura Romana', 'LitRoman', 6, 120),
  (NEWID(), (SELECT id FROM grupe WHERE numar_grupa = 103), (SELECT id FROM utilizator WHERE email = 'ion.popescu@univ.com'), 2, 'Programare Orientata pe Obiect', 'OOP', 7, 180),
  (NEWID(), (SELECT id FROM grupe WHERE numar_grupa = 104), (SELECT id FROM utilizator WHERE email = 'ana.georgescu@univ.com'), 2, 'Contabilitate Financiara', 'ContFin', 5, 150),
  (NEWID(), (SELECT id FROM grupe WHERE numar_grupa = 105), (SELECT id FROM utilizator WHERE email = 'ioana.popa@univ.com'), 1, 'Fizica Generala', 'PhysGen', 6, 120),
  (NEWID(), (SELECT id FROM grupe WHERE numar_grupa = 106), (SELECT id FROM utilizator WHERE email = 'mihai.ionescu@univ.com'), 1, 'Chimie Inorganica', 'ChemInorg', 6, 120),
  (NEWID(), (SELECT id FROM grupe WHERE numar_grupa = 107), (SELECT id FROM utilizator WHERE email = 'elena.radu@univ.com'), 1, 'Biologie Cellulara', 'BioCell', 6, 120),
  (NEWID(), (SELECT id FROM grupe WHERE numar_grupa = 108), (SELECT id FROM utilizator WHERE email = 'vasile.luca@univ.com'), 2, 'Medicina Generala', 'MedGen', 7, 180),
  (NEWID(), (SELECT id FROM grupe WHERE numar_grupa = 109), (SELECT id FROM utilizator WHERE email = 'mihai.ionescu@univ.com'), 2, 'Drept Constitutional', 'DreptCons', 6, 120),
  (NEWID(), (SELECT id FROM grupe WHERE numar_grupa = 110), (SELECT id FROM utilizator WHERE email = 'andrei.cojocaru@univ.com'), 2, 'Arta Contemporana', 'ArtCont', 6, 120),
  (NEWID(), (SELECT id FROM grupe WHERE numar_grupa = 111), (SELECT id FROM utilizator WHERE email = 'gheorghe.mihaila@univ.com'), 1, 'Etica si Deontologie Profesionala', 'EticaProf', 5, 120),
  (NEWID(), (SELECT id FROM grupe WHERE numar_grupa = 112), (SELECT id FROM utilizator WHERE email = 'adriana.tudor@univ.com'), 2, 'Drepturi Fundamentale', 'DreptFund', 6, 150),
  (NEWID(), (SELECT id FROM grupe WHERE numar_grupa = 113), (SELECT id FROM utilizator WHERE email = 'daniela.sava@univ.com'), 1, 'Economia Globala', 'EconGlob', 5, 120),
  (NEWID(), (SELECT id FROM grupe WHERE numar_grupa = 114), (SELECT id FROM utilizator WHERE email = 'gabriel.munteanu@univ.com'), 2, 'Psihologia Invatarii', 'PsihInv', 6, 120),
  (NEWID(), (SELECT id FROM grupe WHERE numar_grupa = 115), (SELECT id FROM utilizator WHERE email = 'lucia.vasilescu@univ.com'), 1, 'Filosofia Stiintifica', 'FilosSti', 6, 180),
  (NEWID(), (SELECT id FROM grupe WHERE numar_grupa = 116), (SELECT id FROM utilizator WHERE email = 'loredana.stanescu@univ.com'), 2, 'Managementul Proiectelor', 'ManProiect', 7, 150),
  (NEWID(), (SELECT id FROM grupe WHERE numar_grupa = 117), (SELECT id FROM utilizator WHERE email = 'radu.ciobanu@univ.com'), 1, 'Statistica Aplicata', 'StatApp', 6, 120),
  (NEWID(), (SELECT id FROM grupe WHERE numar_grupa = 118), (SELECT id FROM utilizator WHERE email = 'marius.dima@univ.com'), 2, 'Marketing Digital', 'MarkDig', 6, 120),
  (NEWID(), (SELECT id FROM grupe WHERE numar_grupa = 119), (SELECT id FROM utilizator WHERE email = 'doru.bucur@univ.com'), 1, 'Programare Web', 'ProgWeb', 6, 120),
  (NEWID(), (SELECT id FROM grupe WHERE numar_grupa = 120), (SELECT id FROM utilizator WHERE email = 'costel.iordache@univ.com'), 2, 'Economie Durabila', 'EcoDurab', 5, 150);

-- 6. Inserare Programări Examene
INSERT INTO programari_examen (id, id_materie, id_profesor, id_student_creator, id_grupa, data_examen, locatie, tip_examen, observatii, status)
VALUES
  (NEWID(), (SELECT id FROM materii WHERE nume = 'Matematica Discreta'), (SELECT id FROM utilizator WHERE email = 'ion.popescu@univ.com'), (SELECT id FROM utilizator WHERE email = 'alex.vasile@univ.com'), (SELECT id FROM grupe WHERE numar_grupa = 101), '2024-06-15 09:00:00', 'Sala 101', 'EXAMEN', 'Examen de nivel mediu', 'IN_ASTEPTARE'),
  (NEWID(), (SELECT id FROM materii WHERE nume = 'Literatura Romana'), (SELECT id FROM utilizator WHERE email = 'ana.georgescu@univ.com'), (SELECT id FROM utilizator WHERE email = 'maria.ionescu@univ.com'), (SELECT id FROM grupe WHERE numar_grupa = 102), '2024-06-16 10:00:00', 'Sala 102', 'EXAMEN', 'Examen semestrial', 'IN_ASTEPTARE'),
  (NEWID(), (SELECT id FROM materii WHERE nume = 'Programare Orientata pe Obiect'), (SELECT id FROM utilizator WHERE email = 'ion.popescu@univ.com'), (SELECT id FROM utilizator WHERE email = 'alex.vasile@univ.com'), (SELECT id FROM grupe WHERE numar_grupa = 103), '2024-06-17 14:00:00', 'Sala 103', 'EXAMEN', 'Examen final pe obiecte', 'IN_ASTEPTARE'),
  (NEWID(), (SELECT id FROM materii WHERE nume = 'Contabilitate Financiara'), (SELECT id FROM utilizator WHERE email = 'ana.georgescu@univ.com'), (SELECT id FROM utilizator WHERE email = 'maria.ionescu@univ.com'), (SELECT id FROM grupe WHERE numar_grupa = 104), '2024-06-18 09:00:00', 'Sala 104', 'EXAMEN', 'Colocviu final', 'IN_ASTEPTARE'),
  (NEWID(), (SELECT id FROM materii WHERE nume = 'Fizica Generala'), (SELECT id FROM utilizator WHERE email = 'ion.popescu@univ.com'), (SELECT id FROM utilizator WHERE email = 'alex.vasile@univ.com'), (SELECT id FROM grupe WHERE numar_grupa = 105), '2024-06-19 10:00:00', 'Sala 105', 'EXAMEN', 'Examen semestrial', 'IN_ASTEPTARE'),
  (NEWID(), (SELECT id FROM materii WHERE nume = 'Chimie Inorganica'), (SELECT id FROM utilizator WHERE email = 'ana.georgescu@univ.com'), (SELECT id FROM utilizator WHERE email = 'maria.ionescu@univ.com'), (SELECT id FROM grupe WHERE numar_grupa = 106), '2024-06-20 09:00:00', 'Sala 106', 'EXAMEN', 'Examen de evaluare', 'IN_ASTEPTARE'),
  (NEWID(), (SELECT id FROM materii WHERE nume = 'Biologie Cellulara'), (SELECT id FROM utilizator WHERE email = 'ion.popescu@univ.com'), (SELECT id FROM utilizator WHERE email = 'alex.vasile@univ.com'), (SELECT id FROM grupe WHERE numar_grupa = 107), '2024-06-21 10:00:00', 'Sala 107', 'EXAMEN', 'Examen de verificare', 'IN_ASTEPTARE'),
  (NEWID(), (SELECT id FROM materii WHERE nume = 'Medicina Generala'), (SELECT id FROM utilizator WHERE email = 'ana.georgescu@univ.com'), (SELECT id FROM utilizator WHERE email = 'maria.ionescu@univ.com'), (SELECT id FROM grupe WHERE numar_grupa = 108), '2024-06-22 14:00:00', 'Sala 108', 'EXAMEN', 'Colocviu de evaluare', 'IN_ASTEPTARE'),
  (NEWID(), (SELECT id FROM materii WHERE nume = 'Drept Constitutional'), (SELECT id FROM utilizator WHERE email = 'ion.popescu@univ.com'), (SELECT id FROM utilizator WHERE email = 'alex.vasile@univ.com'), (SELECT id FROM grupe WHERE numar_grupa = 109), '2024-06-23 09:00:00', 'Sala 109', 'EXAMEN', 'Examen final de semestru', 'IN_ASTEPTARE'),
  (NEWID(), (SELECT id FROM materii WHERE nume = 'Arta Contemporana'), (SELECT id FROM utilizator WHERE email = 'ana.georgescu@univ.com'), (SELECT id FROM utilizator WHERE email = 'maria.ionescu@univ.com'), (SELECT id FROM grupe WHERE numar_grupa = 110), '2024-06-24 10:00:00', 'Sala 110', 'EXAMEN', 'Examen de evaluare finală', 'IN_ASTEPTARE'),
  (NEWID(), (SELECT id FROM materii WHERE nume = 'Etica si Deontologie Profesionala'), (SELECT id FROM utilizator WHERE email = 'ion.popescu@univ.com'), (SELECT id FROM utilizator WHERE email = 'alex.vasile@univ.com'), (SELECT id FROM grupe WHERE numar_grupa = 111), '2024-06-25 09:00:00', 'Sala 111', 'EXAMEN', 'Examen semestrial', 'IN_ASTEPTARE'),
  (NEWID(), (SELECT id FROM materii WHERE nume = 'Drepturi Fundamentale'), (SELECT id FROM utilizator WHERE email = 'ana.georgescu@univ.com'), (SELECT id FROM utilizator WHERE email = 'maria.ionescu@univ.com'), (SELECT id FROM grupe WHERE numar_grupa = 112), '2024-06-26 14:00:00', 'Sala 112', 'EXAMEN', 'Examen de nivel mediu', 'IN_ASTEPTARE'),
  (NEWID(), (SELECT id FROM materii WHERE nume = 'Statistica Aplicata'), (SELECT id FROM utilizator WHERE email = 'ion.popescu@univ.com'), (SELECT id FROM utilizator WHERE email = 'alex.vasile@univ.com'), (SELECT id FROM grupe WHERE numar_grupa = 113), '2024-07-01 09:00:00', 'Sala 113', 'EXAMEN', 'Examen teoretic', 'IN_ASTEPTARE'),
  (NEWID(), (SELECT id FROM materii WHERE nume = 'Marketing Digital'), (SELECT id FROM utilizator WHERE email = 'ana.georgescu@univ.com'), (SELECT id FROM utilizator WHERE email = 'maria.ionescu@univ.com'), (SELECT id FROM grupe WHERE numar_grupa = 114), '2024-07-02 14:00:00', 'Sala 114', 'EXAMEN', 'Proiect final', 'IN_ASTEPTARE'),
  (NEWID(), (SELECT id FROM materii WHERE nume = 'Programare Web'), (SELECT id FROM utilizator WHERE email = 'ion.popescu@univ.com'), (SELECT id FROM utilizator WHERE email = 'alex.vasile@univ.com'), (SELECT id FROM grupe WHERE numar_grupa = 115), '2024-07-03 09:00:00', 'Sala 115', 'EXAMEN', 'Examen aplicativ', 'IN_ASTEPTARE'),
  (NEWID(), (SELECT id FROM materii WHERE nume = 'Economie Durabila'), (SELECT id FROM utilizator WHERE email = 'ana.georgescu@univ.com'), (SELECT id FROM utilizator WHERE email = 'maria.ionescu@univ.com'), (SELECT id FROM grupe WHERE numar_grupa = 116), '2024-07-04 10:00:00', 'Sala 116', 'EXAMEN', 'Examen aplicat', 'IN_ASTEPTARE');

-- 7. Inserare Grupe Utilizator
INSERT INTO grupe_utilizator (id_utilizator, id_grupa, este_sef_semigrupa)
VALUES
  ((SELECT id FROM utilizator WHERE email = 'ion.popescu@univ.com'), (SELECT id FROM grupe WHERE numar_grupa = 101), 0),
  ((SELECT id FROM utilizator WHERE email = 'maria.ionescu@univ.com'), (SELECT id FROM grupe WHERE numar_grupa = 102), 0),
  ((SELECT id FROM utilizator WHERE email = 'alex.vasile@univ.com'), (SELECT id FROM grupe WHERE numar_grupa = 103), 0),
  ((SELECT id FROM utilizator WHERE email = 'ana.georgescu@univ.com'), (SELECT id FROM grupe WHERE numar_grupa = 104), 0),
  ((SELECT id FROM utilizator WHERE email = 'ioana.popa@univ.com'), (SELECT id FROM grupe WHERE numar_grupa = 105), 0),
  ((SELECT id FROM utilizator WHERE email = 'mihai.ionescu@univ.com'), (SELECT id FROM grupe WHERE numar_grupa = 106), 0),
  ((SELECT id FROM utilizator WHERE email = 'elena.radu@univ.com'), (SELECT id FROM grupe WHERE numar_grupa = 107), 0),
  ((SELECT id FROM utilizator WHERE email = 'vasile.luca@univ.com'), (SELECT id FROM grupe WHERE numar_grupa = 108), 0),
  ((SELECT id FROM utilizator WHERE email = 'gheorghe.mihaila@univ.com'), (SELECT id FROM grupe WHERE numar_grupa = 109), 0),
  ((SELECT id FROM utilizator WHERE email = 'andrei.cojocaru@univ.com'), (SELECT id FROM grupe WHERE numar_grupa = 110), 0),
  ((SELECT id FROM utilizator WHERE email = 'sofia.rusu@univ.com'), (SELECT id FROM grupe WHERE numar_grupa = 111), 0),
  ((SELECT id FROM utilizator WHERE email = 'marius.dima@univ.com'), (SELECT id FROM grupe WHERE numar_grupa = 112), 0),
  ((SELECT id FROM utilizator WHERE email = 'adriana.tudor@univ.com'), (SELECT id FROM grupe WHERE numar_grupa = 113), 0),
  ((SELECT id FROM utilizator WHERE email = 'doru.bucur@univ.com'), (SELECT id FROM grupe WHERE numar_grupa = 114), 0),
  ((SELECT id FROM utilizator WHERE email = 'daniela.sava@univ.com'), (SELECT id FROM grupe WHERE numar_grupa = 115), 0),
  ((SELECT id FROM utilizator WHERE email = 'gabriel.munteanu@univ.com'), (SELECT id FROM grupe WHERE numar_grupa = 116), 0),
  ((SELECT id FROM utilizator WHERE email = 'lucia.vasilescu@univ.com'), (SELECT id FROM grupe WHERE numar_grupa = 117), 0),
  ((SELECT id FROM utilizator WHERE email = 'loredana.stanescu@univ.com'), (SELECT id FROM grupe WHERE numar_grupa = 118), 0),
  ((SELECT id FROM utilizator WHERE email = 'radu.ciobanu@univ.com'), (SELECT id FROM grupe WHERE numar_grupa = 119), 0),
  ((SELECT id FROM utilizator WHERE email = 'costel.iordache@univ.com'), (SELECT id FROM grupe WHERE numar_grupa = 120), 0);
