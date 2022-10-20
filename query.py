from rdflib import Graph
from rdflib.plugins.stores.sparqlstore import SPARQLStore

# Create a Graph, pare in Internet data
dbpedia_url = "https://dbpedia.org/sparql"
dbpedia_store = SPARQLStore(dbpedia_url, context_aware=False) # not sure why c_a=False
g = Graph(dbpedia_store)

# Query the data in g using SPARQL
# This query returns the 'name' of all ``foaf:Person`` instances
q = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX dbp: <http://dbpedia.org/ontology/>
SELECT * WHERE {
?city rdf:type <http://dbpedia.org/class/yago/WikicatCitiesInTexas> ;
dbp:populationTotal ?popTotal ;
rdfs:label ?name
OPTIONAL {?city dbp:populationMetro ?popMetro. }
FILTER (?popTotal > 50000 && lang(?name) = "en")
}
"""

# Apply the query to the graph and iterate through results
for r in g.query(q):
    print(r)