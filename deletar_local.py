import sys 
from pymongo import MongoClient
from bson.objectid import ObjectId
import requests
from requests.auth import HTTPDigestAuth

client = MongoClient(host='localhost', port=27017)
db = client['treinamento']

deletes =  list(db.pessoa.find().sort('idade', -1).limit(1))

for delete in deletes:
    db.pessoa.remove({'id': delete['id']})