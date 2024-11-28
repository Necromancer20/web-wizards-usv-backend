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
  (NEWID(), 'Facultatea de Drept'),
  (NEWID(), 'Facultatea de Medicina'),
  (NEWID(), 'Facultatea de Biologie'),
  (NEWID(), 'Facultatea de Fizica'),
  (NEWID(), 'Facultatea de Chimie'),
  (NEWID(), 'Facultatea de Teologie'),
  (NEWID(), 'Facultatea de Psihologie'),
  (NEWID(), 'Facultatea de Sociologie'),
  (NEWID(), 'Facultatea de Arhitectura'),
  (NEWID(), 'Facultatea de Arte'),
  (NEWID(), 'Facultatea de Educatie Fizica si Sport'),
  (NEWID(), 'Facultatea de Turism'),
  (NEWID(), 'Facultatea de Tehnologia Informatiei'),
  (NEWID(), 'Facultatea de Matematica Aplicata'),
  (NEWID(), 'Facultatea de Statistica'),
  (NEWID(), 'Facultatea de Inginerie Civila');

-- 2. Inserare Specializări
INSERT INTO specializari (id, id_facultate, nume)
VALUES
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Matematica si Informatica'), 'Informatica'),
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Litere'), 'Filologie'),
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Inginerie'), 'Automatica si Calculatoare'),
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Stiinte Economice'), 'Contabilitate'),
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Drept'), 'Drept Penal'),
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Medicina'), 'Medicina Generala'),
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Biologie'), 'Biologie Moleculara'),
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Fizica'), 'Fizica Teoretica'),
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Chimie'), 'Chimie Organica'),
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Teologie'), 'Teologie Ortodoxa'),
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Psihologie'), 'Psihologie Clinica'),
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Sociologie'), 'Sociologie Aplicata'),
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Arhitectura'), 'Arhitectura'),
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Arte'), 'Arte Plastice'),
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Educatie Fizica si Sport'), 'Educatie Fizica'),
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Turism'), 'Turism si Ospitalitate'),
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Tehnologia Informatiei'), 'Informatica Aplicata'),
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Matematica Aplicata'), 'Matematica Computationala'),
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Statistica'), 'Statistica si Analiza Datelor');

-- 3. Inserare Grupe
INSERT INTO grupe (id, id_facultate, id_specializare, an, numar_grupa, litera_semigrupa)
VALUES
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Matematica si Informatica'), (SELECT id FROM specializari WHERE nume = 'Informatica'), 1, 101, 1),
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Litere'), (SELECT id FROM specializari WHERE nume = 'Filologie'), 1, 102, 2),
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Inginerie'), (SELECT id FROM specializari WHERE nume = 'Automatica si Calculatoare'), 2, 103, 1),
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Stiinte Economice'), (SELECT id FROM specializari WHERE nume = 'Contabilitate'), 2, 104, 2),
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Drept'), (SELECT id FROM specializari WHERE nume = 'Drept Penal'), 3, 105, 1),
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Medicina'), (SELECT id FROM specializari WHERE nume = 'Medicina Generala'), 3, 106, 2),
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Biologie'), (SELECT id FROM specializari WHERE nume = 'Biologie Moleculara'), 4, 107, 1),
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Fizica'), (SELECT id FROM specializari WHERE nume = 'Fizica Teoretica'), 4, 108, 2),
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Chimie'), (SELECT id FROM specializari WHERE nume = 'Chimie Organica'), 5, 109, 1),
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Teologie'), (SELECT id FROM specializari WHERE nume = 'Teologie Ortodoxa'), 5, 110, 2),
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Psihologie'), (SELECT id FROM specializari WHERE nume = 'Psihologie Clinica'), 6, 111, 1),
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Sociologie'), (SELECT id FROM specializari WHERE nume = 'Sociologie Aplicata'), 6, 112, 2),
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Arhitectura'), (SELECT id FROM specializari WHERE nume = 'Arhitectura'), 7, 113, 1),
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Arte'), (SELECT id FROM specializari WHERE nume = 'Arte Plastice'), 7, 114, 2),
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Educatie Fizica si Sport'), (SELECT id FROM specializari WHERE nume = 'Educatie Fizica'), 8, 115, 1),
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Turism'), (SELECT id FROM specializari WHERE nume = 'Turism si Ospitalitate'), 8, 116, 2),
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Tehnologia Informatiei'), (SELECT id FROM specializari WHERE nume = 'Informatica Aplicata'), 9, 117, 1),
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Matematica Aplicata'), (SELECT id FROM specializari WHERE nume = 'Matematica Computacionala'), 9, 118, 2),
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Statistica'), (SELECT id FROM specializari WHERE nume = 'Statistica si Analiza Datelor'), 10, 119, 1);

-- 4. Inserare Materii
INSERT INTO materii (id, id_facultate, nume)
VALUES
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Matematica si Informatica'), 'Algoritmi si Structuri de Date'),
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Litere'), 'Literatura Romana'),
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Inginerie'), 'Sisteme Digitale'),
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Stiinte Economice'), 'Managementul Afacerilor'),
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Drept'), 'Drept Constitutional'),
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Medicina'), 'Anatomie'),
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Biologie'), 'Genetica'),
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Fizica'), 'Mecanica Teoretica'),
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Chimie'), 'Chimie Anorganica'),
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Teologie'), 'Istoria Bisericii Ortodoxe'),
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Psihologie'), 'Teorii ale Personalitatii'),
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Sociologie'), 'Metode de Cercetare Sociala'),
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Arhitectura'), 'Design Arhitectural'),
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Arte'), 'Istoria Artelor'),
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Educatie Fizica si Sport'), 'Teoria Sporturilor'),
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Turism'), 'Marketing in Turism'),
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Tehnologia Informatiei'), 'Programare Web'),
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Matematica Aplicata'), 'Modelarea Statistica'),
  (NEWID(), (SELECT id FROM facultati WHERE nume = 'Facultatea de Statistica'), 'Teoria Probabilitatilor');

-- 5. Inserare Utilizatori
INSERT INTO utilizator (id, nume, prenume, email, parola, rol)
VALUES
  (NEWID(), 'Ion', 'Popescu', 'ion.popescu@univ.com', 'parola123', 'STUDENT'),
  (NEWID(), 'Maria', 'Ionescu', 'maria.ionescu@univ.com', 'parola123', 'STUDENT'),
  (NEWID(), 'George', 'Vasile', 'george.vasile@univ.com', 'parola123', 'STUDENT'),
  (NEWID(), 'Elena', 'Constantinescu', 'elena.constantinescu@univ.com', 'parola123', 'STUDENT'),
  (NEWID(), 'Andrei', 'Dumitru', 'andrei.dumitru@univ.com', 'parola123', 'STUDENT'),
  (NEWID(), 'Ana', 'Popa', 'ana.popa@univ.com', 'parola123', 'STUDENT'),
  (NEWID(), 'Vasile', 'Mihaila', 'vasile.mihaila@univ.com', 'parola123', 'STUDENT'),
  (NEWID(), 'Ioana', 'Toma', 'ioana.toma@univ.com', 'parola123', 'STUDENT'),
  (NEWID(), 'Alexandru', 'Bucur', 'alexandru.bucur@univ.com', 'parola123', 'STUDENT'),
  (NEWID(), 'Gabriela', 'Ionescu', 'gabriela.ionescu@univ.com', 'parola123', 'STUDENT'),
  (NEWID(), 'Mihai', 'Popa', 'mihai.popa@univ.com', 'parola123', 'STUDENT'),
  (NEWID(), 'Adriana', 'Iancu', 'adriana.iancu@univ.com', 'parola123', 'STUDENT'),
  (NEWID(), 'Cristian', 'Pascu', 'cristian.pascu@univ.com', 'parola123', 'STUDENT'),
  (NEWID(), 'Larisa', 'Ilie', 'larisa.ilie@univ.com', 'parola123', 'STUDENT'),
  (NEWID(), 'Dan', 'Radu', 'dan.radu@univ.com', 'parola123', 'STUDENT'),
  (NEWID(), 'Mihaila', 'Sima', 'mihaila.sima@univ.com', 'parola123', 'STUDENT'),
  (NEWID(), 'Emilia', 'Stanescu', 'emilia.stanescu@univ.com', 'parola123', 'STUDENT'),
  (NEWID(), 'Doru', 'Bucur', 'doru.bucur@univ.com', 'parola123', 'STUDENT'),
  (NEWID(), 'Corina', 'Rusu', 'corina.rusu@univ.com', 'parola123', 'STUDENT');

-- 6. Inserare Programări Examen
INSERT INTO programari_examen (id, id_utilizator, id_materie, data, id_grupa)
VALUES
  (NEWID(), (SELECT id FROM utilizator WHERE nume = 'Ion' AND prenume = 'Popescu'), (SELECT id FROM materii WHERE nume = 'Algoritmi si Structuri de Date'), '2024-12-15 09:00:00', (SELECT id FROM grupe WHERE numar_grupa = 101)),
  (NEWID(), (SELECT id FROM utilizator WHERE nume = 'Maria' AND prenume = 'Ionescu'), (SELECT id FROM materii WHERE nume = 'Literatura Romana'), '2024-12-16 10:00:00', (SELECT id FROM grupe WHERE numar_grupa = 102)),
  (NEWID(), (SELECT id FROM utilizator WHERE nume = 'George' AND prenume = 'Vasile'), (SELECT id FROM materii WHERE nume = 'Sisteme Digitale'), '2024-12-17 11:00:00', (SELECT id FROM grupe WHERE numar_grupa = 103)),
  (NEWID(), (SELECT id FROM utilizator WHERE nume = 'Elena' AND prenume = 'Constantinescu'), (SELECT id FROM materii WHERE nume = 'Managementul Afacerilor'), '2024-12-18 12:00:00', (SELECT id FROM grupe WHERE numar_grupa = 104)),
  (NEWID(), (SELECT id FROM utilizator WHERE nume = 'Andrei' AND prenume = 'Dumitru'), (SELECT id FROM materii WHERE nume = 'Drept Constitutional'), '2024-12-19 14:00:00', (SELECT id FROM grupe WHERE numar_grupa = 105)),
  (NEWID(), (SELECT id FROM utilizator WHERE nume = 'Ana' AND prenume = 'Popa'), (SELECT id FROM materii WHERE nume = 'Anatomie'), '2024-12-20 09:00:00', (SELECT id FROM grupe WHERE numar_grupa = 106)),
  (NEWID(), (SELECT id FROM utilizator WHERE nume = 'Vasile' AND prenume = 'Mihaila'), (SELECT id FROM materii WHERE nume = 'Genetica'), '2024-12-21 10:00:00', (SELECT id FROM grupe WHERE numar_grupa = 107)),
  (NEWID(), (SELECT id FROM utilizator WHERE nume = 'Ioana' AND prenume = 'Toma'), (SELECT id FROM materii WHERE nume = 'Mecanica Teoretica'), '2024-12-22 11:00:00', (SELECT id FROM grupe WHERE numar_grupa = 108)),
  (NEWID(), (SELECT id FROM utilizator WHERE nume = 'Alexandru' AND prenume = 'Bucur'), (SELECT id FROM materii WHERE nume = 'Chimie Anorganica'), '2024-12-23 12:00:00', (SELECT id FROM grupe WHERE numar_grupa = 109)),
  (NEWID(), (SELECT id FROM utilizator WHERE nume = 'Gabriela' AND prenume = 'Ionescu'), (SELECT id FROM materii WHERE nume = 'Istoria Bisericii Ortodoxe'), '2024-12-24 14:00:00', (SELECT id FROM grupe WHERE numar_grupa = 110)),
  (NEWID(), (SELECT id FROM utilizator WHERE nume = 'Mihai' AND prenume = 'Popa'), (SELECT id FROM materii WHERE nume = 'Teorii ale Personalitatii'), '2024-12-25 09:00:00', (SELECT id FROM grupe WHERE numar_grupa = 111)),
  (NEWID(), (SELECT id FROM utilizator WHERE nume = 'Adriana' AND prenume = 'Iancu'), (SELECT id FROM materii WHERE nume = 'Metode de Cercetare Sociala'), '2024-12-26 10:00:00', (SELECT id FROM grupe WHERE numar_grupa = 112)),
  (NEWID(), (SELECT id FROM utilizator WHERE nume = 'Cristian' AND prenume = 'Pascu'), (SELECT id FROM materii WHERE nume = 'Design Arhitectural'), '2024-12-27 11:00:00', (SELECT id FROM grupe WHERE numar_grupa = 113)),
  (NEWID(), (SELECT id FROM utilizator WHERE nume = 'Larisa' AND prenume = 'Ilie'), (SELECT id FROM materii WHERE nume = 'Istoria Artelor'), '2024-12-28 12:00:00', (SELECT id FROM grupe WHERE numar_grupa = 114)),
  (NEWID(), (SELECT id FROM utilizator WHERE nume = 'Dan' AND prenume = 'Radu'), (SELECT id FROM materii WHERE nume = 'Teoria Sporturilor'), '2024-12-29 14:00:00', (SELECT id FROM grupe WHERE numar_grupa = 115)),
  (NEWID(), (SELECT id FROM utilizator WHERE nume = 'Mihaila' AND prenume = 'Sima'), (SELECT id FROM materii WHERE nume = 'Marketing in Turism'), '2024-12-30 09:00:00', (SELECT id FROM grupe WHERE numar_grupa = 116)),
  (NEWID(), (SELECT id FROM utilizator WHERE nume = 'Emilia' AND prenume = 'Stanescu'), (SELECT id FROM materii WHERE nume = 'Programare Web'), '2024-12-31 10:00:00', (SELECT id FROM grupe WHERE numar_grupa = 117)),
  (NEWID(), (SELECT id FROM utilizator WHERE nume = 'Doru' AND prenume = 'Bucur'), (SELECT id FROM materii WHERE nume = 'Modelarea Statistica'), '2025-01-01 11:00:00', (SELECT id FROM grupe WHERE numar_grupa = 118)),
  (NEWID(), (SELECT id FROM utilizator WHERE nume = 'Corina' AND prenume = 'Rusu'), (SELECT id FROM materii WHERE nume = 'Teoria Probabilitatilor'), '2025-01-02 12:00:00', (SELECT id FROM grupe WHERE numar_grupa = 119));

-- 7. Inserare Grupe Utilizator
INSERT INTO grupe_utilizator (id, id_utilizator, id_grupa)
VALUES
  (NEWID(), (SELECT id FROM utilizator WHERE nume = 'Ion' AND prenume = 'Popescu'), (SELECT id FROM grupe WHERE numar_grupa = 101)),
  (NEWID(), (SELECT id FROM utilizator WHERE nume = 'Maria' AND prenume = 'Ionescu'), (SELECT id FROM grupe WHERE numar_grupa = 102)),
  (NEWID(), (SELECT id FROM utilizator WHERE nume = 'George' AND prenume = 'Vasile'), (SELECT id FROM grupe WHERE numar_grupa = 103)),
  (NEWID(), (SELECT id FROM utilizator WHERE nume = 'Elena' AND prenume = 'Constantinescu'), (SELECT id FROM grupe WHERE numar_grupa = 104)),
  (NEWID(), (SELECT id FROM utilizator WHERE nume = 'Andrei' AND prenume = 'Dumitru'), (SELECT id FROM grupe WHERE numar_grupa = 105)),
  (NEWID(), (SELECT id FROM utilizator WHERE nume = 'Ana' AND prenume = 'Popa'), (SELECT id FROM grupe WHERE numar_grupa = 106)),
  (NEWID(), (SELECT id FROM utilizator WHERE nume = 'Vasile' AND prenume = 'Mihaila'), (SELECT id FROM grupe WHERE numar_grupa = 107)),
  (NEWID(), (SELECT id FROM utilizator WHERE nume = 'Ioana' AND prenume = 'Toma'), (SELECT id FROM grupe WHERE numar_grupa = 108)),
  (NEWID(), (SELECT id FROM utilizator WHERE nume = 'Alexandru' AND prenume = 'Bucur'), (SELECT id FROM grupe WHERE numar_grupa = 109)),
  (NEWID(), (SELECT id FROM utilizator WHERE nume = 'Gabriela' AND prenume = 'Ionescu'), (SELECT id FROM grupe WHERE numar_grupa = 110)),
  (NEWID(), (SELECT id FROM utilizator WHERE nume = 'Mihai' AND prenume = 'Popa'), (SELECT id FROM grupe WHERE numar_grupa = 111)),
  (NEWID(), (SELECT id FROM utilizator WHERE nume = 'Adriana' AND prenume = 'Iancu'), (SELECT id FROM grupe WHERE numar_grupa = 112)),
  (NEWID(), (SELECT id FROM utilizator WHERE nume = 'Cristian' AND prenume = 'Pascu'), (SELECT id FROM grupe WHERE numar_grupa = 113)),
  (NEWID(), (SELECT id FROM utilizator WHERE nume = 'Larisa' AND prenume = 'Ilie'), (SELECT id FROM grupe WHERE numar_grupa = 114)),
  (NEWID(), (SELECT id FROM utilizator WHERE nume = 'Dan' AND prenume = 'Radu'), (SELECT id FROM grupe WHERE numar_grupa = 115)),
  (NEWID(), (SELECT id FROM utilizator WHERE nume = 'Mihaila' AND prenume = 'Sima'), (SELECT id FROM grupe WHERE numar_grupa = 116)),
  (NEWID(), (SELECT id FROM utilizator WHERE nume = 'Emilia' AND prenume = 'Stanescu'), (SELECT id FROM grupe WHERE numar_grupa = 117)),
  (NEWID(), (SELECT id FROM utilizator WHERE nume = 'Doru' AND prenume = 'Bucur'), (SELECT id FROM grupe WHERE numar_grupa = 118)),
  (NEWID(), (SELECT id FROM utilizator WHERE nume = 'Corina' AND prenume = 'Rusu'), (SELECT id FROM grupe WHERE numar_grupa = 119));
