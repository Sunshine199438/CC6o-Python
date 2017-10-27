from pymongo import MongoClient

client = MongoClient('localhost',27017)
db = client['unifeg']
alunos = db['alunos']


#para inserir docs em lote na collection usa-se uma lista de dicts
lista = [
      {
        "nome" : "ze maria"
        "email" : "zmaria@outlook.com"
        "programacao" : ["C++", "Python", "java"]
        },{
        "Nome":"pedro paulo pedrosa"
        "email":"pedrosa@pp.com"
        "programçao" : ["python","json", "R"]
        },{
        "Nome":"pedro paulo pedrosa"
        "email":"pedrosa@pp.com"
        "programçao" : ["python","json", "R"]
        }
]

#ze_maria_id = alunos.insert_one(ze_maria)
#faz a inserção por lotes (todos docs) e retorna lista de todos ids de nv docs
result = alunos.insert_many(lista)
print(result.inserted_ids)
