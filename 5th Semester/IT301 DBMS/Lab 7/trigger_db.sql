-- Exercise 1

CREATE TABLE Student_marks
(
    Student_id int,
    Sname varchar(100),
    Sub1 int,
    Sub2 int,
    Sub3 int,
    Sub4 int,
    Sub5 int,
    Total int,
    Per_marks decimal(5,2),
    Grade varchar(20)
);

INSERT INTO Student_marks 
VALUES 
    (1, 'Steven King', 0, 0, 0, 0, 0, 0, 0.00, '');
INSERT INTO Student_marks
VALUES
    (2, 'Neena Kochhar', 0, 0, 0, 0, 0, 0, 0.00, '');
INSERT INTO Student_marks
VALUES
    (3, 'Lex De Haan', 0, 0, 0, 0, 0, 0, 0.00, '');
INSERT INTO Student_marks
VALUES
    (4, 'Alexander Hunold', 0, 0, 0, 0, 0, 0, 0.00, '');


DROP TRIGGER IF EXISTS update_student_marks;
DELIMITER //
CREATE TRIGGER update_student_marks
    BEFORE UPDATE ON Student_marks 
    FOR EACH ROW 
    BEGIN
        SET NEW.Total = (NEW.Sub1 + NEW.Sub2 + NEW.Sub3 + NEW.Sub4 + NEW.Sub5);
        SET NEW.Per_marks = (NEW.Total/5);
        SET NEW.Grade = CASE
            WHEN New.Per_marks >= 90.00 THEN 'Excellent'
            WHEN New.Per_marks >= 75.00 THEN 'Very Good'
            WHEN New.Per_marks >= 60.00 THEN 'Good'
            WHEN New.Per_marks >= 40.00 THEN 'Average'
            WHEN New.Per_marks < 40.00 THEN 'Not Promoted'
        END;
    END
//
DELIMITER ;


-- Exercise 2


CREATE TABLE Blog
(
    Id int,
    Title varchar(20),
    Content varchar(200),
    Deleted int
);

CREATE TABLE Audit
( 
    Id int NOT NULL AUTO_INCREMENT,
    Blog_id int,
    Changetype enum('NEW','EDIT','DELETE') NOT NULL,
    Changetime timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (Id)
);

DROP TRIGGER IF EXISTS insert_audit;
DELIMITER //
CREATE TRIGGER insert_audit
    AFTER INSERT ON Blog 
    FOR EACH ROW
    BEGIN
        IF NEW.Deleted = 0 THEN
            INSERT INTO Audit (Blog_id, Changetype) VALUES(New.Id, 'NEW');
        ELSE
            INSERT INTO Audit (Blog_id, Changetype) VALUES(New.Id, 'DELETE');   
        END IF;
    END
//
DELIMITER ;

DROP TRIGGER IF EXISTS update_audit;
DELIMITER //
CREATE TRIGGER update_audit
    AFTER UPDATE ON Blog 
    FOR EACH ROW
    BEGIN
        IF NEW.Deleted = 0 THEN
            INSERT INTO Audit (Blog_id, Changetype) VALUES(New.Id, 'EDIT');
        ELSE
            INSERT INTO Audit (Blog_id, Changetype) VALUES(New.Id, 'DELETE');   
        END IF;
    END
//
DELIMITER ;


-- Exercise 3

CREATE TABLE Patient
(
    Id int,
    Pname varchar(100)
);

CREATE TABLE Room
(
    Id int,
    Rname varchar(100),
    Status varchar(10),
    Pid int
);

CREATE TABLE Medicine
(
    Id int,
    Mname varchar(100),
    Pid int
);

CREATE TABLE Bill
(
    Id int,
    Amount decimal(5,2),
    Pid int
);

INSERT INTO Patient
VALUES
    (1, 'John Doe');

INSERT INTO Room
VALUES
    (1, 'Room 1', 'Full', 1);

INSERT INTO Medicine
VALUES
    (1, 'Ranboxy', 1);

INSERT INTO Bill
VALUES
    (1, 10.00, 1);


DROP TRIGGER IF EXISTS delete_patient;
DELIMITER //
CREATE TRIGGER delete_patient
    AFTER DELETE ON Patient 
    FOR EACH ROW 
    BEGIN
        DELETE FROM Medicine WHERE Pid = Old.Id;
        DELETE FROM Bill WHERE Pid = Old.Id;
        UPDATE Room SET Pid = NULL, Status = 'Empty' WHERE Pid = Old.Id;
    END
//
DELIMITER ;