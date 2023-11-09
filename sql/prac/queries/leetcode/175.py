# Write a solution to report the first name, last name, city, and state of each person in the Person table. If the address of a personId is not present in the Address table, report null instead.

# Return the result table in any order.


query = '''SELECT
p.firstName as firstName,
p.lastName as lastName,
a.city as city,
a.state as state
FROM Person p
LEFT JOIN Address a
ON p.personId = a.personId;
'''