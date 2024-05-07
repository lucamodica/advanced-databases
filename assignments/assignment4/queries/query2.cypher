// query 2: Find the names of all students who worked as teaching assistants in courses given by the D3-2 division in study period 2 in academic year 2023/2024.
match (s:Student)
match (s)-[:workAsTA]->(ta:TeachingAssistant)
match (th:TeacherHours)-[:teacherHoursIn]->(ta)

match (th)-[:courseHoursIn]->(cInstance:CourseInstance)
where cInstance.courseInstanceAcademicYear = "2023-2024"
    and cInstance.studyPeriod = 2

match (cInstance)-[:courseInstanceOf]->(c:Course)
match (c)-[:courseBelongsTo]->(d:Division)
where d.divisionName = "D3-2"

return s.studentName as studentName