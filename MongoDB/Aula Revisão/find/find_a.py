
from pymongo import MongoClient
import pprint

client = MongoClient('localhost',27017)
db = client['unifeg']
alunos = db['alunos']

#sellete com where
doc_a = alunos.find_one({"email" : "zmaria@outlook.com"})
pprint.pprint(doc_a)


#busca um documento do inicio da collection
doc_a = alunos.find_one()
#pprint.pprint(doc_a) #print bunitinho do dicionario/documento
#print(type(doc_a))
#print (doc_a['nome'])
#print (doc_a['email'])
#print (doc_a['programacao'])
#print (len(doc_a['programacao']))
#print (type(doc_a['programacao']))
