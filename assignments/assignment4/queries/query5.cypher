// query 5: Find all programmes along with the total number of owned courses. 
// List the results in descending order of number of owned courses.
MATCH (course:Course)
MATCH (course)-[:courseOwnedBy]->(programme:Programme)
WITH  programme, COUNT(course) AS numberOfCourses
RETURN programme.programmeCode AS programmeCode,
        programme.programmeName AS programmeName,
        numberOfCourses
ORDER BY numberOfCourses  DESC