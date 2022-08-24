from elasticsearch import Elasticsearch, helpers
import configparser

config = configparser.ConfigParser()
config.read('elastic.ini')

es = Elasticsearch(
      cloud_id=config['ELASTIC']['cloud_id'],
      basic_auth=(config['ELASTIC']['user'], config['ELASTIC']['password'])
)

es.info()