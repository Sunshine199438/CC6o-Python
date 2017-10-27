#Ap pyhton p trabalhar com mongo
#Select e Update
import pymongo as mg  #este eh o drive do mongo

#PASSO 02
#Proximo passo criar mongodb
clientDB = mg.MongoClient('localhost','27017')

#PASSO 03
#informar qual é o nome do banco "Shema" que estára sendo acessado
db = clientDB['aula'] #Aula é o shema

#PASSO 04
#Definir qual é a collection que está sendo acessado
aluno_c = db['aluno']

#PASSO 05-01
#criando um documento json para insserir no mongo
aluno_01 = {"nome":"zé",
"idade":"18",
"sexo":"M","email":"zé@email.com"}

#PASSO 06-02
#inserindo o documento json no mongodb
anluno_id = aluno_c.insert_one(aluno_01).inserted_id



print anluno_id
print '. | FINAL'
