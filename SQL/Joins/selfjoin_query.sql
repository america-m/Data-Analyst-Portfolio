SELECT 
a1.district,
a1.address,
a2.address
FROM
address a1
INNER JOIN address a2
ON a1.address > a2.address; 
