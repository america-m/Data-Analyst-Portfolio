SELECT * FROM store_locations 
INTERSECT 
SELECT * FROM most_popular_locations
ORDER BY city;