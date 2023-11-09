SELECT Department,Employee,Salary
FROM (SELECT
e.name AS Employee,
d.name AS Department,
e.salary AS Salary,
DENSE_RANK() OVER (PARTITION BY d.name ORDER BY e.salary DESC) AS srank
FROM Employee e
JOIN Department d
ON e.departmentId = d.id) AS subquery
WHERE srank < 4;