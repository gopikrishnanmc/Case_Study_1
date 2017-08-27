from rdflib.graph import ConjunctiveGraph

ns = """
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX owl: <http://www.w3.org/2002/07/owl#>
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
    PREFIX foaf:<http://xmlns.com/foaf/0.1/>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX rp: <http://www.semanticweb.org/abjb788/ontologies/2015/3/untitled-ontology-208#>
    """


def add_model():
    global g
    g = ConjunctiveGraph()
    g.parse("Dental_pain_model-2017-01-31-V1.ttl", format="turtle")



def insert1():
    g.update(ns + '''
    INSERT  {?Observation1 rp:hasObservationStatus rp:9_ObservationPresent}
    WHERE{
    ?Observation1 a rp:Pain_present.
    }
    ''')


def delete1():
    g.update(ns + '''
    DELETE  {?Observation1 rp:hasObservationStatus rp:9_ObservationPresent}
    WHERE{
    ?Observation1 a rp:Pain_absent.
    }
    ''')


def insert2():
    g.update(ns + '''
    INSERT  {?Observation1 rp:hasObservationStatus rp:9_ObservationPresent}
    WHERE{
    ?Observation1 a rp:Pain_absent.
    }
    ''')


def delete2():
    g.update(ns + '''
    DELETE {?Observation1 rp:hasObservationStatus rp:9_ObservationPresent}
    WHERE{
    ?Observation1 a rp:Pain_present.
    }
    ''')


def insertDSModel():
    try:
        g.update(ns + '''
        INSERT {?Diagnosis rp:hasDiagnosisObsWeight ?DiagnosisObsWeight}
        WHERE
        {SELECT (SUM (?Weight)AS ?DiagnosisObsWeight) ?Diagnosis
        {?Diagnosis ?property ?Observation.
        ?property rdfs:subPropertyOf rp:Observation_Diagnosis_properties.
        ?Observation rp:hasWeight ?Weight.
        ?Observation rp:hasObservationStatus rp:9_ObservationPresent.
        }
        GROUP BY ?Diagnosis
        }
        ''')
    except:
        return ("Click Add Model")


def deleteDSModel():
    g.update(ns + '''
        DELETE {?Diagnosis rp:hasDiagnosisObsWeight ?DiagnosisObsWeight}
        WHERE
        {?Diagnosis ?property ?Observation.
        }
        ''')


def view():
    qres = g.query(ns + """
    SELECT ?Label ?DiagnosisWeight
    WHERE
    {
        ?PulpalDiagnosis  rp:hasDiagnosisObsWeight ?DiagnosisWeight.
        ?PulpalDiagnosis a ?Diagnosis.
        ?Diagnosis rdfs:subClassOf* rp:Pulpal_Disease.
        ?Diagnosis rdfs:label ?Label
        } ORDER BY desc (?DiagnosisWeight)
    """)

    #for row in qres:
        #print(" %s hasDiagnosis %s" % row)
    return (qres)


def clear():
    qres = g.update(ns + """
    CLEAR SILENT DEFAULT;
    """)


add_model()
# insert()
# insertDSModel()
# view()
# print(view())
