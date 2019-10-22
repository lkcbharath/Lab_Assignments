-- Exercise 1
DELIMITER 
&&;

CREATE PROCEDURE usp_get_employees(IN target_salary INT) 
BEGIN
    SELECT first_name, last_name 
    FROM employee 
    WHERE salary >= target_salary;
END 
&&

DELIMITER 
;

CALL usp_get_employees(48100);

-- Exercise 2

DELIMITER
&&;

CREATE PROCEDURE usp_get_employees(IN target_salary INT)
BEGIN
    SELECT first_name, last_name
    FROM employee
    WHERE salary >= target_salary;
END
&&

DELIMITER 
;

CALL usp_get_employees
(48100)

-- Exercise 3

-- Exercise 4

-- Exercise 5

-- Exercise 6

