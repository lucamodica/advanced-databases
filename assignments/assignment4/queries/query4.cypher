// query 4: Find all students registered for course instance I-910 that were not 
// registered for course instance I-911.
match (registration:Registration)-[:registrationContainsInstance]->(courseInstance:CourseInstance {instanceId: "I-910"}),
      (registration)-[:studentRegistered]->(student:Student)
optional match (student)-[:studentRegistered]->(registration2:Registration)-[:registrationContainsInstance]->(courseInstance2:CourseInstance {instanceId: "I-911"})
with student, courseInstance2
where courseInstance2 is null
return student.studentId as studentId, student.studentName AS studentName