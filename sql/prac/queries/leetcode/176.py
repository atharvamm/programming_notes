# Write a solution to find the second highest salary from the Employee table. If there is no second highest salary, return null (return None in Pandas).

# Write your MySQL query statement below
query = '''
SELECT 
IFNULL((SELECT DISTINCT salary
FROM Employee
ORDER BY salary DESC
LIMIT 1 OFFSET 1),NULL) AS SecondHighestSalary;
'''