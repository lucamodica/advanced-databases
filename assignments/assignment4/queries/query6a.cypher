// query 6a: Find the number of: senior teachers
match (seniorTeacher:SeniorTeacher)
with COUNT(seniorTeacher) as numberOfSeniorTeachers
return numberOfSeniorTeachers