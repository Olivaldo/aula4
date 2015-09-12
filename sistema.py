# coding: UTF-8
# !/usr/bin/python

import sys 
from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient(host='localhost', port=27017)
db = client['treinamento']

#db.tabela1.insert({'nome':'Olivaldo', 'idade':34})
#db.tabela1.insert({'nome':'Carlos', 'idade':32})
#db.tabela1.insert({'nome':'Bruno', 'idade':30})

#print list(db.tabela1.find())
#print list(db.tabela1.find({'nome': {'$regex': '.*o|O.*'}}))
#print list(db.tabela1.find({'idade': {'$gt': 31, '$lt': 60}}))
#print list(db.tabela1.find({'idade': {'$in': [32, 30, 34]}}).sort('nome'))
#objeto = db.tabela1.find({'and' : {'nome'}})
#print objeto.count()

#chave = ['nome']
#condicao = {'idade' : {'$gte' : 30}}
#inicial = {'contador' : 0, 'soma' : 0}
#funcao = 'function(doc, out) {out.contador++; out.soma += doc.idade;}'  
#print list(db.tabela1.group(chave, condicao, inicial, funcao))

#objetos = db.tabela1.aggregate(
#    [{
#        '$group': {
#            '_id' : '$nome',
#            'idade': {'$sum': '$idade'},
#            'media': {'$avg': '$idade'},
#            'contador': {'$sum': 1}
#        }
#    }]
#)

#objetos1 = db.tabela1.aggregate(
#    [{
#        '$group': {
#            '_id' : '$nome',
#            'idade': {'$sum': '$idade'},
#            'media': {'$avg': '$idade'},
#            'contador': {'$sum': 1}
#        }
#    }]
#)

#for objeto in objetos:
#    print objeto

#print ' '

#for objeto1 in objetos:
#    print objeto1['_id'] + ' = ' + str(objeto1['idade'])

#db.tabela1.remove({'idade': {'$gt': 34}}, True)
db.tabela1.remove({'_id': '55f44911fb7925125da619ec'}, True)
db.tabela1.remove({'_id': ObjectId('55f44a72fb7925126beb9d93')})
db.tabela1.update({'nome': 'Olivaldo'}, {'$set': {'idade': 0}})

print list(db.tabela1.find().max())