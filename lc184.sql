--
-- @lc app=leetcode.cn id=184 lang=mysql
--
-- [184] 部门工资最高的员工
--

-- @lc code=start
# Write your MySQL query statement below
SELECT t.Department as Department, e.Name as Employee, t.Salary
FROM `employee` e JOIN (
    SELECT Max(Salary) AS Salary, DepartmentId, department.Name as Department
    FROM `employee` JOIN `department`
    ON DepartmentId = department.Id
    GROUP BY DepartmentId
) t
ON t.Salary = e.Salary AND t.DepartmentId = e.DepartmentId
-- @lc code=end

