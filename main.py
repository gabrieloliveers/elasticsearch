from poplib import POP3_SSL_PORT
from elasticsearch import Elasticsearch
from datetime import datetime #importa a datetime pra quando inserir o arquivo me falar a hora que foi inserido

es = Elasticsearch(
    ['127.0.1.1'],
    POP3_SSL_PORT=9200,
)
#me tras as informações do elastic local
print(es.info())

#aqui eu to criando uma variavel com os dados do documento que eu quero inserir
doc = {
    'Nome': 'gabriel',
    'Idade': 23,
    'Email': 'gr.oliveira99@gmail.com',
    'Formação': 'sistemas de informação',
    'Habilidades': ['python', 'aws', 'linux', 'terraform'],
    'Timestamp': datetime.now(),
}    

#aqui faz a inserção dos dados da variável no documento
res = es.index(index="data-elasticsearch", id=1, body=doc)
print("Status da inserção: ", res['result']) 

#aqui eu faço um get trazendo os dados do arquivo e ainda mostra a hora que foi inserido os dados
res = es.get(index="data-elasticsearch", id=1)
print("\n\n")
print(res['_source'])