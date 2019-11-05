Select * FROM Student_marks;

UPDATE Student_marks SET Sub1 = 90, Sub2 = 100 WHERE Student_id = 1;

Select * FROM Student_marks;

-- 

Select * FROM Audit;

INSERT INTO Blog VALUES(1, 'My first article', 'Sumne', 0);
UPDATE Blog SET Title = 'My second' WHERE Id = 1;

Select * FROM Audit;

-- 


Select * from Patient, Room, Medicine, Bill;

DELETE FROM Patient WHERE Id = 1;

Select * from Room;