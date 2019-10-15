-- Exercise 1

CREATE OR REPLACE VIEW TNS AS SELECT mo.title AS "Movie_Title", re.name AS "Reviewer_Name", ra.stars as "Rating" FROM Movie mo, Reviewer re, Rating ra WHERE mo.mID = ra.mID AND re.rID = ra.rID;

SELECT MAX(mo.year) AS "Latest Year of Review" FROM Movie mo, TNS tns WHERE mo.title = tns.Movie_Title AND tns.Reviewer_Name = "Chris Jackson";

-- Exercise 2

CREATE OR REPLACE VIEW RatingStats AS SELECT Movie_Title, COUNT(*) AS "Number_of_Ratings", AVG(Rating) AS "Average_Rating" FROM TNS GROUP BY Movie_Title HAVING COUNT(*) > 1;

SELECT Movie_Title FROM RatingStats WHERE Average_Rating = (SELECT MAX(Average_Rating) FROM RatingStats WHERE Number_of_Ratings >= 3);

-- Exercise 3

CREATE OR REPLACE VIEW Favourites AS SELECT re.rID, mo.mID, ra.stars FROM Movie mo, Reviewer re, Rating ra WHERE mo.mID = ra.mID AND re.rID = ra.rID AND ra.stars = (SELECT MAX(Stars) FROM Rating WHERE rID = re.rID);

SELECT DISTINCT
    CASE WHEN re1.name > re2.name THEN re2.name ELSE re1.name END AS "Reviewer 1", 
    CASE WHEN re1.name < re2.name THEN re2.name ELSE re1.name END AS "Reviewer 2",
    mo.title AS "Movie"
FROM Reviewer re1, Reviewer re2, Movie mo WHERE re1.rID IN (SELECT rID FROM Favourites WHERE mID = 
mo.mID) AND re2.rID IN (SELECT rID FROM Favourites WHERE mID = mo.mID) AND re1.rID != re2.rID; 

-- fa.rID, re.rID, mo.mID FROM Favourites fa, Movie mo, Reviewer re WHERE ;