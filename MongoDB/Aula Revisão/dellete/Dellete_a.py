from pymongo import MongoClient

client = MongoClient('localhost',27017)
db = client['unifeg']
alunos = db['alunos']

result = alunos.delete_manu({"email":"pedrosa@pp.com"})