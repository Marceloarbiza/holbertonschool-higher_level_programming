-- 3 first students in the Batch ID=3
-- because Batich 3 is the best!
SELECT id,name FROM cities
WHERE state_id = (
        SELECT id
        FROM states
        WHERE name = 'California')
ORDER BY cities.id ASC;
