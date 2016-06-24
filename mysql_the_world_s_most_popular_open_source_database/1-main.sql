SELECT 'Number of seasons by tvshow_id?' AS '';
SELECT tvshow_id, count(id) FROM Season GROUP BY tvshow_id;

SELECT 'Number of occurrences of the same episode number ordered by episode number?' AS '';
SELECT number, count(id) FROM Episode GROUP BY number;

SELECT 'Top 3 of the Genre\'s occurrences in all TVShows ordered by this number?' AS '';
SELECT genre_id, count(*) as 'occurrences_genre' FROM TVShowGenre GROUP BY genre_id ORDER BY count(*) DESC LIMIT 3;

SELECT 'Search all TVShow with this letter sequence \'th\' case insensitive and display with the name in lowercase?' AS '';
SELECT LOWER(name) as 'name' FROM TVShow WHERE name LIKE '%th%';