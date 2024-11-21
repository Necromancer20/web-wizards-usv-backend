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
  (NEWID(), 'Facultatea de Stiinte Economice');

-- 2. Inserare Specializări
INSERT INTO specializari (id, id_facultate, nume)
VALUES
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Matematica si Informatica'), 'Informatica'),
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Litere'), 'Filologie'),
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Inginerie'), 'Automatica si Calculatoare'),
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Stiinte Economice'), 'Contabilitate');

-- 3. Inserare Grupe
INSERT INTO grupe (id, id_facultate, id_specializare, an, numar_grupa, litera_semigrupa)
VALUES
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Matematica si Informatica'), (SELECT id FROM specializari WHERE nume = 'Informatica'), 1, 101, 1),
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Litere'), (SELECT id FROM specializari WHERE nume = 'Filologie'), 1, 102, 2),
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Inginerie'), (SELECT id FROM specializari WHERE nume = 'Automatica si Calculatoare'), 2, 103, 1),
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Stiinte Economice'), (SELECT id FROM specializari WHERE nume = 'Contabilitate'), 2, 104, 2);

-- 4. Inserare Utilizatori (Profesori, Studenti)
INSERT INTO utilizator (id, first_name, last_name, email, password, rol)
VALUES
  (NEWID(), 'Ion', 'Popescu', 'ion.popescu@univ.com', 'parola123', 'professor'),
  (NEWID(), 'Maria', 'Ionescu', 'maria.ionescu@univ.com', 'parola123', 'student'),
  (NEWID(), 'Alex', 'Vasile', 'alex.vasile@univ.com', 'parola123', 'student'),
  (NEWID(), 'Ana', 'Georgescu', 'ana.georgescu@univ.com', 'parola123', 'professor');

-- 5. Inserare Materii
INSERT INTO materii (id, id_grupa, id_profesor, semestrul, nume, nume_abreviat, numar_credite, durata_examen_minute)
VALUES
  (NEWID(), (SELECT id FROM grupe WHERE numar_grupa = 101), (SELECT id FROM utilizator WHERE email = 'ion.popescu@univ.com'), 1, 'Matematica Discreta', 'MathDiscr', 6, 120),
  (NEWID(), (SELECT id FROM grupe WHERE numar_grupa = 102), (SELECT id FROM utilizator WHERE email = 'ana.georgescu@univ.com'), 1, 'Literatura Romana', 'LitRoman', 6, 120),
  (NEWID(), (SELECT id FROM grupe WHERE numar_grupa = 103), (SELECT id FROM utilizator WHERE email = 'ion.popescu@univ.com'), 2, 'Programare Orientata pe Obiect', 'OOP', 7, 180),
  (NEWID(), (SELECT id FROM grupe WHERE numar_grupa = 104), (SELECT id FROM utilizator WHERE email = 'ana.georgescu@univ.com'), 2, 'Contabilitate Financiara', 'ContFin', 5, 150);

-- 6. Inserare Programări Examen
INSERT INTO programari_examen (id, id_materie, id_profesor, id_student_creator, id_grupa, data_examen, locatie, tip_examen, observatii, status)
VALUES
(NEWID(), (SELECT id FROM materii WHERE nume = 'Matematica Discreta'), (SELECT id FROM utilizator WHERE email = 'ion.popescu@univ.com'), (SELECT id FROM utilizator WHERE email = 'alex.vasile@univ.com'), (SELECT id FROM grupe WHERE numar_grupa = 101), '2024-12-15 10:00:00', 'Sala 101', 'examen', 'Examen de nivel mediu', 'in_asteptare'),
(NEWID(), (SELECT id FROM materii WHERE nume = 'Literatura Romana'), (SELECT id FROM utilizator WHERE email = 'ana.georgescu@univ.com'), (SELECT id FROM utilizator WHERE email = 'maria.ionescu@univ.com'), (SELECT id FROM grupe WHERE numar_grupa = 102), '2024-12-16 14:00:00', 'Sala 102', 'coloc', 'Colocviu final', 'in_asteptare'),
(NEWID(), (SELECT id FROM materii WHERE nume = 'Programare Orientata pe Obiect'), (SELECT id FROM utilizator WHERE email = 'ion.popescu@univ.com'), (SELECT id FROM utilizator WHERE email = 'alex.vasile@univ.com'), (SELECT id FROM grupe WHERE numar_grupa = 103), '2024-12-17 09:00:00', 'Sala 103', 'examen', 'Examen final pe obiecte', 'in_asteptare'),
(NEWID(), (SELECT id FROM materii WHERE nume = 'Contabilitate Financiara'), (SELECT id FROM utilizator WHERE email = 'ana.georgescu@univ.com'), (SELECT id FROM utilizator WHERE email = 'maria.ionescu@univ.com'), (SELECT id FROM grupe WHERE numar_grupa = 104), '2024-12-18 12:00:00', 'Sala 104', 'coloc', 'Colocviu de evaluare', 'in_asteptare');

-- 7. Inserare Grupe Utilizator
INSERT INTO grupe_utilizator (id_utilizator, id_grupa, este_sef_semigrupa)
VALUES
  ((SELECT id FROM utilizator WHERE email = 'ion.popescu@univ.com'), (SELECT id FROM grupe WHERE numar_grupa = 101), 1),
  ((SELECT id FROM utilizator WHERE email = 'maria.ionescu@univ.com'), (SELECT id FROM grupe WHERE numar_grupa = 102), 0),
  ((SELECT id FROM utilizator WHERE email = 'alex.vasile@univ.com'), (SELECT id FROM grupe WHERE numar_grupa = 103), 0),
  ((SELECT id FROM utilizator WHERE email = 'ana.georgescu@univ.com'), (SELECT id FROM grupe WHERE numar_grupa = 104), 1);
