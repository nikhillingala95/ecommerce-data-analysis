SELECT product, SUM(quantity) 
FROM sales 
GROUP BY product;
