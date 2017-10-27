#Passos basicos para o mongo

from pymongo import MongoClient  #importa a classe que cria a conexão com servidor

#Passo 1 Conexão com Servidor
client = MongoClient('localhost',27017)

#Passo 2 Selecao do banco de dados dentro do servidor
db = client['unifeg'] #client - servidor, unifeg o bando dentro do server

#Passo 3 dentro do banco selecionar a collection
alunos = db['alunos']

# toda inserção/operação do mongodb é json
ze_maria = {
        "nome" : "ze maria",
        "email" : "zmaria@outlook.com",
        "programacao" : ["C++", "Python", "java"]
}

pedro_pp = {
    "Nome":"pedro paulo pedrosa",
    "email":"pedrosa@pp.com",
    "programçao" : ["python","json", "R"]
}

#insere um documento(dic)na collection informada
ze_maria_id = alunos.insert_one(ze_maria)
pedro_pp_id = alunos.insert_one(pedro_pp)

#print (type(ze+maria)) #Mostra que Zé_maria é um dicionario vale lembrar
#que um dicioario é uma conbinação de chave/valor como um doc Json
