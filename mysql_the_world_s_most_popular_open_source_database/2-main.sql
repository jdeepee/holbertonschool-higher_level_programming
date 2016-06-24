SELECT 'Number of season by TVShow ordered by name (A-Z)?' AS '';
SELECT TVShow.name, count(Season.tvshow_id) AS nb_seasons FROM TVShow LEFT JOIN Season ON (TVShow.id = Season.tvshow_id) GROUP BY Season.tvshow_id ORDER BY name;

SELECT 'List of Network by TVShow ordered by name (A-Z)?' AS '';
SELECT TVShow.name AS "TVShow name", Network.name AS "Network name" FROM TVShow LEFT JOIN Network ON (TVShow.network_id = Network.id) ORDER BY TVShow.name;

SELECT 'List of TVShows ordered by name (A-Z) in the Network \'Fox (US)\'?' AS '';
SELECT TVShow.name FROM TVShow LEFT JOIN Network ON (TVShow.network_id = Network.id) ORDER BY TVShow.name;

SELECT 'Number of episodes by TVShows ordered by name (A-Z)?' AS '';
SELECT TVShow.name, count(Episode.id) AS nb_episodes FROM TVShow LEFT JOIN Season ON (TVShow.id = Season.tvshow_id) LEFT JOIN Episode ON (Season.id = Episode.season_id) GROUP BY TVShow.id ORDER BY TVShow.name;
