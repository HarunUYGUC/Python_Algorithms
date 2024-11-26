""" https://leetcode.com/problems/employees-earning-more-than-their-managers/ """

SELECT E1.name as Employee
FROM Employee as E1, Employee as E2
WHERE E1.managerId = E2.id and E1.salary > E2.salary
