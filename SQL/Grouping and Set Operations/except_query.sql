SELECT * FROM store_locations 
EXCEPT 
SELECT * FROM most_popular_locations
ORDER BY city;