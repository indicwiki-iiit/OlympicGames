from rdflib import Graph
from SPARQLWrapper import SPARQLWrapper, JSON, N3, CSV
from pprint import pprint
import pandas as pd

sparql = SPARQLWrapper("https://dbpedia.org/sparql/")

AthletesDF = pd.read_csv('../New_Athletes_With_Attributes.csv')

# To extract Date of Births
Date_OfBirths = []
for ind in AthletesDF.index[:1]:
    print(ind)
    query = "SELECT ?abstract WHERE {?athlete rdfs:label \"" + AthletesDF['Label'][
        ind] + "\"@en. ?athlete dbo:abstract ?abstract.}"
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    queryResult = sparql.query().convert()
    if len(queryResult['results']['bindings']) == 0:
        # birthDate.append("None")
        print("None")
    else:
        l = []
        for result in queryResult['results']['bindings']:
            l.append(result['birthDate']['value'])
        # birthDate.append(l[0])
        print(l[0])
