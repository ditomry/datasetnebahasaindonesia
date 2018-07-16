from rdflib import Graph
from rdflib.namespace import Namespace
from rdflib.term import URIRef

g = Graph()
g.parse("idwiki-20130508-instance-types.nt", format="nt")

person = open( "person.txt", "w+")
org = open( "org.txt", "w+")
place = open( "place.txt", "w+")
	
	
for subj, pred, obj in g:
	if (obj) in ("http://dbpedia.org/ontology/Person"):
		newLine = subj.replace("http://id.dbpedia.org/resource/", "").replace("_", " ").encode('utf-8') + "\n"
		person.write(newLine)
	if (obj) in ("http://dbpedia.org/ontology/Organisation"):
		newLine = subj.replace("http://id.dbpedia.org/resource/", "").replace("_", " ").encode('utf-8') + "\n"
		org.write(newLine) 
	if (obj) in ("http://dbpedia.org/ontology/Place"):
		newLine = subj.replace("http://id.dbpedia.org/resource/", "").replace("_", " ").encode('utf-8') + "\n"
		place.write(newLine) 