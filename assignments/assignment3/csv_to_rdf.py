import csv
from rdflib import Graph, Namespace, Literal, URIRef
from rdflib.namespace import RDF, RDFS, XSD

# metadata (file path, class name, class identifier attribute)
metadata = {
  "Student": {
    "file_path": "data/Students.csv",
    "class_name": "Student",
    "class_id": "ID"
  },
  "SeniorTeacher": {
    "file_path": "data/Senior_Teachers.csv",
    "class_name": "SeniorTeacher",
    "class_id": "ID"
  },
  "ReportedHour": {
    "file_path": "data/Reported_Hours.csv",
    "class_name": "ReportedHour",
    "class_id": "ID"
  },
  "Registration": {
    "file_path": "data/Registrations.csv",
    "class_name": "Registration",
    "class_id": "ID"
  },
  "Programme": {
    "file_path": "data/Programmes.csv",
    "class_name": "Programme",
    "class_id": "ID"
  },
  "ProgrammeCourse": {
    "file_path": "data/Programme_Courses.csv",
    "class_name": "ProgrammeCourse",
    "class_id": "ID"
  },
  "Course": {
    "file_path": "data/Courses.csv",
    "class_name": "Course",
    "class_id": "ID"
  },
  "CoursePlanning": {
    "file_path": "data/Course_plannings.csv",
    "class_name": "CoursePlanning",
    "class_id": "ID"
  },
  "CourseInstance": {
    "file_path": "data/Course_Instances.csv",
    "class_name": "CourseInstance",
    "class_id": "ID"
  },
  "AssignedHour": {
    "file_path": "data/Assigned_Hours.csv",
    "class_name": "AssignedHour",
    "class_id": "ID"
  }
}

# Create a Graph
g = Graph()

# Define the namespace
ex = Namespace("http://example.org/")
g.bind("ex", ex)

# Load the ontology
g.parse("ontology.ttl", format="turtle")

# Function to convert a CSV file to Turtle RDF triples
def csv_to_rdf(class_metadata):
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            subject = URIRef(ex + row['ID'])
            g.add((subject, RDF.type, ex[class_name]))
            for key, value in row.items():
                if key != 'ID':
                    g.add((subject, ex[key], Literal(value)))

# Convert each CSV file to Turtle RDF triples
csv_to_rdf("data/Students.csv", "Student")
csv_to_rdf("data/Senior_Teachers.csv", "SeniorTeacher")
csv_to_rdf("data/Reported_Hours.csv", "ReportedHour")
csv_to_rdf("data/Registrations.csv", "Registration")
csv_to_rdf("data/Programmes.csv", "Programme")
csv_to_rdf("data/Programme_Courses.csv", "ProgrammeCourse")
csv_to_rdf("data/Courses.csv", "Course")
csv_to_rdf("data/Course_plannings.csv", "CoursePlanning")
csv_to_rdf("data/Course_Instances.csv", "CourseInstance")
csv_to_rdf("data/Assigned_Hours.csv", "AssignedHour")

# Serialize the triples to a Turtle file
g.serialize("all_triples.ttl", format="turtle")

# Serialize the triples for each CSV file separately
# the values are: csv_file, class_name, class_identifier_attribute
for csv_file, class_name, class_id in metadata:
    g_csv = Graph()
    g_csv.bind("ex", ex)
    g_csv.parse("ontology.ttl", format="turtle")
    csv_to_rdf(csv_file, class_name)
    g_csv.serialize(f"{csv_file[:-4]}.ttl", format="turtle")