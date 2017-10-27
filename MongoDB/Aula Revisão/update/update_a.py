
from pymongo import MongoClient
import pprint

client = MongoClient('localhost',27017)
db = client['unifeg']
alunos = db['alunos']


tonho = alunos.find_one({"email":"pedrosa@pp.com"})
pprint.pprint(tonho)

tonho['nome'] = 'Antonio jose' #Atualizando o nome

tonho['rg'] = '123456789'#adicionando coluna 

tonho ['programacao'].append ('Js') #altualisando lista 
alunos.save(tonho)
