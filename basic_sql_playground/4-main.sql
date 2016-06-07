INSERT INTO eyescolor (person_id, color) VALUES (6, "Brown");
INSERT INTO eyescolor (person_id, color) VALUES (7, "Green");

CREATE TABLE TVShow (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name char(128) NOT NULL
);

CREATE TABLE TVShowPerson (
    tvshow_id INTEGER NOT NULL,
    person_id INTEGER NOT NULL,
    FOREIGN KEY(person_id) REFERENCES Person(id),
    FOREIGN KEY(tvshow_id) REFERENCES tvshow(id)
);

INSERT INTO tvshow (name) VALUES ("Homeland");
INSERT INTO tvshow (name) VALUES ("The big bang theory");
INSERT INTO tvshow (name) VALUES ("Game of Thrones");
INSERT INTO tvshow (name) VALUES ("Breaking bad");
INSERT INTO tvshowperson (person_id, tvshow_id) VALUES (4, 2);
INSERT INTO tvshowperson (person_id, tvshow_id) VALUES (3, 3);
INSERT INTO tvshowperson (person_id, tvshow_id) VALUES (2, 4);
INSERT INTO tvshowperson (person_id, tvshow_id) VALUES (3, 5);
INSERT INTO tvshowperson (person_id, tvshow_id) VALUES (3, 6);
INSERT INTO tvshowperson (person_id, tvshow_id) VALUES (3, 7);
SELECT * FROM person;
SELECT * FROM eyescolor;
SELECT * FROM tvshow;
SELECT * FROM tvshowperson;