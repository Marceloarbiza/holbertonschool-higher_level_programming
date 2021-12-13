-- 3 first students in the Batch ID=3
-- because Batich 3 is the best!
SELECT title
FROM tv_shows WHERE tv_shows.id NOT IN (
SELECT tv_shows.id FROM tv_shows
INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
INNER JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id WHERE tv_genres.name = 'Comedy')
ORDER BY title;