import sys 
from pymongo import MongoClient
from bson.objectid import ObjectId
import requests
from requests.auth import HTTPDigestAuth

r = requests.get('http://apiolivaldo.herokuapp.com/api/pessoa/', auth=('admin', 'admin'))
objetos = r.json()['results']
#print objetos

client = MongoClient(host='localhost', port=27017)
db = client['treinamento']
db.pessoa.drop()
    
for objeto in objetos:
  db.pessoa.insert({'id': objeto['id'], 'nome': objeto['nome'], 'idade': objeto['idade']})  

print list(db.pessoa.find())

print list(db.pessoa.find().sort('idade', -1).limit(1))

deletes =  list(db.pessoa.find().sort('idade', -1).limit(1))

for delete in deletes:
    db.pessoa.remove({'id': delete['id']})
