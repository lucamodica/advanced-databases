import csv
from rdflib import Graph, URIRef, Literal, Namespace, RDF

# Initialize a graph
g = Graph()

# Define namespaces
base_uri = Namespace("http://example.org/resource/")
rdf_type = RDF.type
schema = Namespace("http://example.org/schema/")

# Read CSV file
with open('data/Course_plannings.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Create a URI for each row (entity)
        entity_uri = base_uri + row['id']
        
        # Add type relation based on the table/class mapping
        g.add((URIRef(entity_uri), rdf_type, schema.YourClass))
        
        # Add attributes as RDF properties
        g.add((URIRef(entity_uri), schema.someAttribute, Literal(row['column_name'])))
        
        # Add relationships (assuming 'related_id' is a foreign key to another entity)
        related_entity_uri = base_uri + row['related_id']
        g.add((URIRef(entity_uri), schema.relatedTo, URIRef(related_entity_uri)))

# Serialize the graph in RDF/XML format
print(g.serialize(format='xml').decode('utf-8'))