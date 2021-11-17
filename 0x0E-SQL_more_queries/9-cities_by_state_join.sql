-- 3 first students in the Batch ID=3
-- because Batich 3 is the best!
SELECT cities.id, cities.name, states.name FROM cities
JOIN states ON cities.state_id = states.id;
