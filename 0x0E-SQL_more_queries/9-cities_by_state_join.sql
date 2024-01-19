-- using the join syntax
-- lisintg all cities cnotained in the database
SELECT id, name
FROM cities
INNER JOIN states ON cities.state_id = states.id
ORDER BY id ASC;
