SELECT DISTINCT last_name
FROM person
join (SELECT tvshow_id, person_id AS id FROM tvshowperson) using (id)
WHERE tvshow_id = 3;

SELECT count(*) FROM Person WHERE age > 30;

SELECT Person.id, first_name, last_name, age, Eyescolor.color, TVShow.name FROM Person JOIN TVShowPerson ON Person.id=TVShowPerson.person_id, TVShow ON TVShowPerson.tvshow_id=TVShow.id, Eyescolor ON Eyescolor.person_id=Person.id;

SELECT SUM(age) FROM Person;