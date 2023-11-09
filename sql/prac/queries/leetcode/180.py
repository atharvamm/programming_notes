# Find all numbers that appear at least three times consecutively.

# Return the result table in any order.


# Write your MySQL query statement below

# SELECT DISTINCT num,
# LAG(num, 1, 0) OVER (ORDER BY id) AS prev,
# LEAD(num, 1, 0) OVER (ORDER BY id) AS next
# FROM Logs
# WHERE prev = num AND num = next
# ORDER BY id;


SELECT DISTINCT num AS ConsecutiveNums
FROM (
    SELECT id, 
          num,
           LAG(num, 1, 0) OVER (ORDER BY id) AS prev,
           LEAD(num, 1, 0) OVER (ORDER BY id) AS next
    FROM Logs
) AS subquery
WHERE prev = num AND num = next
ORDER BY id;
