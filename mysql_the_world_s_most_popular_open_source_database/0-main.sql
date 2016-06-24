SELECT 'List of all tables?' AS '';
show tables;

SELECT 'Display the table structure of TVShow, Genre and TVShowGenre?' as '';
show create table TVShow;
show create table Genre;
show create table TVShowGenre;

SELECT 'List of TVShows, only id and name ordered by name (A-Z)?' as '';
SELECT id, name FROM TVShow ORDER BY name;

SELECT 'List of Genres, only id and name ordered by name (Z-A)?' as '';
SELECT id, name FROM Genre ORDER BY name;

SELECT 'List of Network, only id and name?' as '';
SELECT id, name FROM Network;

SELECT 'Number of episodes in the database?' as '';
SELECT COUNT(id) FROM Episode;