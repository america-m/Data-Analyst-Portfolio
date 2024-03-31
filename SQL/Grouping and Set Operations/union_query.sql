
SELECT * FROM store_locations
UNION ALL
SELECT * FROM most_popular_locations 
ORDER BY city;

