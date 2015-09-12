import sys 
from pymongo import MongoClient
from bson.objectid import ObjectId
import requests
from requests.auth import HTTPDigestAuth

client = MongoClient(host='localhost', port=27017)
db = client['treinamento']

print list(db.pessoa.find())