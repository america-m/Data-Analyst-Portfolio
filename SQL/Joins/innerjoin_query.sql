SELECT 
  p.customer_id, 
  p.payment_id,
  c.first_name,
  c.last_name,
  c.email
FROM 
  payment p
  LEFT JOIN customer c USING (customer_id) 
WHERE
  c.first_name LIKE 'Jen%'
ORDER BY 
  c.last_name;