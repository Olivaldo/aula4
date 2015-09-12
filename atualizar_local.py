import sys 
from pymongo import MongoClient
from bson.objectid import ObjectId
import requests
from requests.auth import HTTPDigestAuth

client = MongoClient(host='localhost', port=27017)
db = client['treinamento']

db.pessoa.update({'idade': {'$gte': 0}} , {'$set': {'idade': 0}}, multi= True)