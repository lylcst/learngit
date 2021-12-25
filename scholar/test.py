
from elasticsearch import Elasticsearch, helpers
es = Elasticsearch()
query = {
    'query': {
        'match_all': {}
    }
}
print(es.search("scholar", body = query)['hits']['total']['value'])