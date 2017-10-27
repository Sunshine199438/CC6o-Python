
from pymongo import MongoClient
import pprint

client = MongoClient('localhost',27017)
db = client['unifeg']
alunos = db['alunos']

for alunos in alunos.finf():
    pprint.pprint(aluno)

print (' O numeor total de registros é..:' alunos.find().count())
