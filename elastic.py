from elasticsearch import Elasticsearch
import json

es = Elasticsearch(
    ['127.0.1.1:9200']
)

with open('data.json') as elastic_data:
    for line in elastic_data:
        json_line = json.loads(line)  
        res = es.index(index="prorionjson", body=json_line) #só recebe documento, e json
        print("Status da inserção: ", res['result']) 