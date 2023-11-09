# Write a solution to find all dates' Id with higher temperatures compared to its previous dates (yesterday).

# Return the result table in any order.

# The result format is in the following example.


SELECT id AS Id
FROM(SELECT *,
LAG(recordDate,1,NULL) OVER (ORDER BY recordDate) AS prev_date,
LAG(temperature,1,NULL) OVER (ORDER BY recordDate) AS prev_temp
FROM Weather) AS temp_table
WHERE temperature > prev_temp AND DATEDIFF(recordDate,prev_date) = 1;