SELECT 
rental_date,
SUM(amount)amount 
FROM 
payment 
INNER JOIN rental USING (customer_id)
GROUP BY 
rental_date
ORDER BY 
amount; 