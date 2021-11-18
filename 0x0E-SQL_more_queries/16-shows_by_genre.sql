-- 3 first students in the Batch ID=3
-- because Batich 3 is the best!
--SELECT title,name FROM tv_shows
--RIGHT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
--LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
--ORDER BY title ASC;
SELECT tv_shows.title AS title, tv_genres.name AS name
FROM tv_show_genres
RIGHT JOIN tv_shows
ON tv_show_genres.show_id = tv_shows.id
LEFT JOIN tv_genres
ON tv_genres.id = tv_show_genres.genre_id
ORDER BY title, name ASC;
