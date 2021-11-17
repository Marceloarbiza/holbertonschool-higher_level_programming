-- 3 first students in the Batch ID=3
-- because Batich 3 is the best!
SELECT tv_shows.title,tv_show_genres.genre_id FROM hbtn_0d_tvshows
JOIN hbtn_0d_tvshows ON tv_shows.title = tv_show_genres.genre_id;
