from poplib import POP3_SSL_PORT
from elasticsearch import Elasticsearch

es = Elasticsearch(
    ['127.0.1.1'],
    POP3_SSL_PORT=9200,
)
print(es.info())

