SELECT 
title, rating, SUM(replacement_cost) cost
FROM 
film 
GROUP BY title, rating
HAVING SUM(replacement_cost)<10
ORDER BY rating;

