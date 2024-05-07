// query 3: Find all teachers who are assigned more than 120 hours in course 1015 in study period 1 in academic year 2018/2019.
match (th:TeacherHours)-[:teacherHoursIn]->(t:Teacher)
match (th)-[:courseHoursIn]->(cInstance:CourseInstance)-[:courseInstanceOf]->(c:Course {courseCode: 1015})
where cInstance.studyPeriod = 1
    and cInstance.courseInstanceAcademicYear = "2018-2019"
    and th.assignedHours > 120
return t.teacherId as teacherId,
    t.teacherName as teachername,
    th.assignedHours as assignedHours