import numpy as np

my_data = np.arange(0,1000000) #criando o vetor


m1 = np.reshape(my_data, (1000,1000)) #colocando em uma matriz 1000x1000


aki= m1.diagonal() #colocando a diagonal em uma variavel


print (aki.sum()) #printando a somas das diagonais


for az in m1:
    print(a)

#print (m1)

#print (m1[2][:])
