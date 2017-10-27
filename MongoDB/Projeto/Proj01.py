from pymongo import MongoClient 
import pprint

#R1
client = MongoClient('localhost',27017)
#R2
db = client['client']
#R3
cidade = db['cidade']

#R4
client = db['client']

client = [

{
    "cpf":"13235",
    "Nome":"pedro paulo pedrosa",
    "email":"pedrosa@pp.com",
    "gosto" : ["python","json", "R"]
},{
    "cpf":"145345",
    "Nome":"pado paulo pedrosa",
    "email":"pedrosa@pp.com",
    "gosto" : ["python","json", "R"]
},{
    "cpf":"2634565",
    "Nome":"joao paulo pedrosa",
    "email":"pedrosa@pp.com",
    "gosto" : ["python","json", "R"]
},{
    "cpf":"1323456235",
    "Nome":"god paulo pedrosa",
    "email":"pedrosa@pp.com",
    "gosto" : ["python","json", "R"]
},{
    "cpf":"132345235",
    "Nome":"pdd paulo pedrosa",
    "email":"pedrosa@pp.com",
    "gosto" : ["python","json", "R"]
}

]

client = client.insert_many(client)

#R5

porto = {
        "nome" : "ferreira",
        "uf" : "SP",
        "Bairro" : ["caju", "morro", "BR"]
}

nova = {
        "nome" : "rueira",
        "uf" : "PR",
        "Bairro" : ["caju", "morro", "BR"]
}

estor = {
        "nome" : "ferreira",
        "uf" : "SP",
        "Bairro" : ["caju", "morro", "BR"]
}


porto = cidade.insert_one(porto)
nova = cidade.insert_one(nova)
estor = cidade.insert_one(estor)

#R6
result = client.delete_manu({"Nome":"pado paulo pedrosa"})


#R7 
print (cidade['porto'])
print (cidade['nova'])
print (cidade['estor'])