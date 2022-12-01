-- QUERIES FOR HOMEWORK
-- 1. List the following details of each employee: employee number, last name, first name, sex, and salary.

SELECT
	e.emp_no AS employee_number,
	e.last_name,
	e.first_name,
	e.sex,
	s.salary
FROM
	employees e
	JOIN salaries s ON e.emp_no = s.emp_no
ORDER BY
	e.last_name ASC; 
	
-- 2. List first name, last name, and hire date for employees who were hired in 1986.

SELECT
	e.first_name,
	e.last_name,
	e.hire_date
FROM
	employees e
WHERE
	EXTRACT(YEAR FROM e.hire_date) = 1986
ORDER BY
	e.last_name ASC; 

-- 3. List the manager of each department with the following information: department number, 
--    department name, the manager's employee number, last name, first name.

SELECT
	d.dept_no,
	d.dept_name,
	dm.emp_no,
	e.last_name,
	e.first_name
FROM
	departments d
	JOIN dept_manager dm ON d.dept_no = dm.dept_no
	JOIN employees e ON dm.emp_no = e.emp_no
ORDER BY
	e.last_name ASC; 

-- 4. List the department of each employee with the following information: employee number, 
--    last name, first name, and department name.

SELECT
	de.emp_no,
	e.last_name,
	e.first_name,
	d.dept_name
FROM
	departments d
	JOIN dept_emp de ON d.dept_no = de.dept_no
	JOIN employees e ON de.emp_no = e.emp_no
ORDER BY
	e.last_name ASC; 

-- 5. List first name, last name, and sex for employees whose first name is "Hercules" and last names begin with "B."

SELECT
	e.first_name,
	e.last_name,
	e.sex
FROM
	employees e
WHERE
	e.first_name = 'Hercules'
	AND e.last_name LIKE 'B%'
ORDER BY
	e.last_name ASC; 

-- 6. List all employees in the Sales department, including their employee number, last name, first name, and department name.

SELECT
	e.emp_no,
	e.last_name,
	e.first_name,
	d.dept_name
FROM
	departments d
	JOIN dept_emp de ON d.dept_no = de.dept_no
	JOIN employees e ON de.emp_no = e.emp_no
WHERE
	d.dept_name = 'Sales'
ORDER BY
	e.last_name ASC;

-- 7. List all employees in the Sales and Development departments, including 
--    their employee number, last name, first name, and department name.

SELECT
	e.emp_no,
	e.last_name,
	e.first_name,
	d.dept_name
FROM
	departments d
	JOIN dept_emp de ON d.dept_no = de.dept_no
	JOIN employees e ON de.emp_no = e.emp_no
WHERE
	d.dept_name = 'Sales' OR d.dept_name = 'Development'
ORDER BY
	e.last_name ASC;

-- 8. List the frequency count of employee last names (i.e., how many employees share each last name) in descending order.

SELECT
	e.last_name,
	COUNT(*) AS num_emps
FROM
	employees e
GROUP BY
	e.last_name
ORDER BY
	num_emps DESC;
