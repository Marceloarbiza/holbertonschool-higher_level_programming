-- 3 first students in the Batch ID=3
-- because Batich 3 is the best!
SELECT title,name FROM tv_shows
RIGHT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY title ASC;
