#essa caralha de biblioteca não aceitava passar a "port" penei pa carai pra achar e saber 
#que o parametro que passa é esse pop3 dentro da lib pop dos inferno ai pra passar a porta kkkkkkkk
from poplib import POP3_SSL_PORT
from elasticsearch import Elasticsearch
from datetime import datetime #importa a datetime pra quando inserir o arquivo me falar a hora que foi inserido, só pra fica bonitinho

es = Elasticsearch(
    ['127.0.1.1'],
    POP3_SSL_PORT=9200,
)
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

#aqui eu faço um get trazendo os dados do arquivo e ainda mostra a hora que foi inserido os dados, muito doidera né vei kkkkk
res = es.get(index="data-elasticsearch", id=1)
print("\n\n")
print(res['_source'])