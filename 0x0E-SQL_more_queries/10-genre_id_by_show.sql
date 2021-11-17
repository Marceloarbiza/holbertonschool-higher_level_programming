-- 3 first students in the Batch ID=3
-- because Batich 3 is the best!
SELECT tv_shows.title,tv_show_genres.genre_id FROM tvshows
JOIN tvshows ON tv_shows.title = tv_show_genres.genre_id
ORDER BY tv_shows.title,tv_show_genres.genre_id ASC;
