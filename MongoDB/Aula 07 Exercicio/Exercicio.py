''' Criar e insserir dados no mongo usando python '''

import pymongo as mg

clientDB = mg.MongoClient('localhost',27017)

db = clientDB.user

usuario_p = db.user


N = int(raw_input("Informe quantos meliantes voce deseja inserir: "))
count = 0

for i in range(N):
    count = count + 1
    nome = raw_input("Nome do individuo: ")
    idade = raw_input("Idade do individuo: ")
    sexo = raw_input("Sexo do individuo: ")
    email = raw_input("Email do individuo: ")
    celular = raw_input("Celular do individuo: ")
    usuario_x = {"nome": nome, "idade": idade, "sexo": sexo, "email": email, "celular": celular}
    meliante_id = usuario_p.insert_one(usuario_x).inserted_id
    print "-----------------------------------------------------------\n"


print "------------------------------------------------------------"


for post in usuario_p.find():
    print post['nome']
    print post['celular']
    print post['email']
    print "------------------------------------------------------------\n"
