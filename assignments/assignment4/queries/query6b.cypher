// query 6b: Find the number of: all people
call {
  match (teacher:Teacher)
  return teacher.teacherId as id
  union
  match (student:Student)
  return student.studentId as id
}
return count(distinct id) as numberOfPeople