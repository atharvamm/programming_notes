# Write a solution to find the nth highest salary from the Employee table. If there is no nth highest salary, return null.

# The result format is in the following example.



-CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
-BEGIN
-  RETURN (
-      # Write your MySQL query statement below.
-        SELECT 
-        IFNULL((SELECT DISTINCT salary 
-        FROM Employee
-        ORDER BY salary DESC
-        LIMIT 1 OFFSET N),NULL) AS getNthHighestSalary(N);
-
-  );
-END