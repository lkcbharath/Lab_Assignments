-- Exercise 1
DROP PROCEDURE IF EXISTS usp_get_employees;

DELIMITER &&

CREATE PROCEDURE usp_get_employees(IN target_salary INT) 
BEGIN
    SELECT Fname, Lname FROM Employee WHERE Salary >= target_salary;
END &&

DELIMITER ;

CALL usp_get_employees(48100);

-- Exercise 3?
DROP PROCEDURE IF EXISTS usp_get_towns_starting_with;

DELIMITER &&

CREATE PROCEDURE usp_get_towns_starting_with(IN begin_string varchar(100))
BEGIN
    SELECT Dlocation FROM Dept_locations WHERE DLocation LIKE CONCAT(begin_string,'%');
END &&

DELIMITER ;

CALL usp_get_towns_starting_with('H');

-- Exercise 4
DROP FUNCTION IF EXISTS ufn_get_salary_level;

DELIMITER &&

CREATE FUNCTION ufn_get_salary_level(salary int) 
RETURNS varchar(10)
BEGIN
    IF salary < 30000 THEN
        RETURN 'Low';
    END IF;
    IF salary <= 50000 THEN
        RETURN 'Average';
    END IF;
    RETURN 'High';
END &&

DELIMITER ;

SELECT ufn_get_salary_level(35000);

-- Exercise 5
DROP PROCEDURE IF EXISTS emp_in_dept;

DELIMITER $$

CREATE PROCEDURE emp_in_dept(IN department INT, INOUT name_result varchar(1000) DEFAULT "")
BEGIN
    DECLARE finished INT DEFAULT 0;
    DECLARE employee_name varchar(100) DEFAULT "";

    DEClARE cursor_emp CURSOR FOR SELECT Fname FROM Employee WHERE Dno = department;
    
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET finished = 1;
    
    OPEN cursor_emp;

    -- REPEAT FETCH cursor_emp INTO employee_name;
    -- UNTIL finished = 1 
    -- END REPEAT;

    e_loop: LOOP
        FETCH cursor_emp INTO employee_name;
        IF finished = 1 THEN
            LEAVE e_loop;
        END IF;     

        SET name_result = CONCAT(employee_name,", ",name_result)

    CLOSE cursor_emp;
END $$

DELIMITER ;

SET @result = "";
CALL emp_in_dept(5,@result);
SELECT @result;

-- Exercise 6

-- DROP PROCEDURE IF EXISTS update_emp_salary;

-- DELIMITER $$
-- CREATE PROCEDURE update_emp_salary()
-- BEGIN
--     DECLARE finished int DEFAULT 0;
--     DECLARE salary varchar(100) DEFAULT = "";

--     DEClARE cursor_emp CURSOR FOR SELECT Fname,Minit,Lname FROM Employee WHERE Dno = department;
    
--     DECLARE CONTINUE HANDLER FOR NOT FOUND SET finished = 1;
    
--     OPEN cursor_emp;

--     GET emp_loop: LOOP
--         FETCH cursor_emp INTO employee_name;
--         IF finished = 1 THEN
--             LEAVE emp_loop;
--         END IF;

--         SET employee_list = CONCAT(employee_name,', ',employee_list);
--     END LOOP emp_loop;

--     CLOSE cursor_emp;
-- END $$
-- DELIMITER ;
