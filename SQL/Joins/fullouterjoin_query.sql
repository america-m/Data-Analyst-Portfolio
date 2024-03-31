SELECT 
  f.title,
  f.description,
  c.category_id,
  c.film_id
FROM 
  film_category c
FULL OUTER JOIN film f
  ON c.film_id = f.film_id


