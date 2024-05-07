// query 1: Find the name, director and department of all programmes.
match (programme:Programme)
match (programme)-[:programmeDirectedBy]->(teacher:SeniorTeacher)
match (programme)-[:programmeBelongsTo]->(department:Department)
return programme.programmeName as programmeName,
       teacher.teacherId as teacherId,
       teacher.teacherName as teacherName,
       department.departmentName as departmentName