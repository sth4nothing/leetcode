--
-- @lc app=leetcode.cn id=185 lang=mysql
--
-- [185] 部门工资前三高的所有员工
--
Create table If Not Exists Employee (Id int, Name varchar(255), Salary int, DepartmentId int);
Create table If Not Exists Department (Id int, Name varchar(255));
Truncate table Employee;
insert into Employee (Id, Name, Salary, DepartmentId) values ('1', 'Joe', '85000', '1');
insert into Employee (Id, Name, Salary, DepartmentId) values ('2', 'Henry', '80000', '2');
insert into Employee (Id, Name, Salary, DepartmentId) values ('3', 'Sam', '60000', '2');
insert into Employee (Id, Name, Salary, DepartmentId) values ('4', 'Max', '90000', '1');
insert into Employee (Id, Name, Salary, DepartmentId) values ('5', 'Janet', '69000', '1');
insert into Employee (Id, Name, Salary, DepartmentId) values ('6', 'Randy', '85000', '1');
insert into Employee (Id, Name, Salary, DepartmentId) values ('7', 'Will', '70000', '1');
Truncate table Department;
insert into Department (Id, Name) values ('1', 'IT');
insert into Department (Id, Name) values ('2', 'Sales');
SELECT * FROM `employee`;
-- @lc code=start
# Write your MySQL query statement below
SELECT department.Name as Department, t.Employee, t.Salary
FROM (
    SELECT DepartmentId, Name AS Employee, IF(@d = (@d:= DepartmentId), @r:= @r + (@s <> Salary), @r:= 1) as Rank, (@s:= Salary) AS Salary
    FROM `employee`, (SELECT @d:=0, @s:=0, @r:= 0) a
    ORDER BY DepartmentId, Salary DESC
) t JOIN `department` ON t.DepartmentId = department.Id
WHERE t.Rank <= 3
ORDER BY t.DepartmentId, t.Salary DESC
-- @lc code=end

