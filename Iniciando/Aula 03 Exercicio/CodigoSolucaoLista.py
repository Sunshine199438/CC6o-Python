
#gpoli 20170810
#resolucao do exercicio da aula 03 - 20170810
#primeira parte pegar a string do usuario
#enquando esta nao for maior que 30 repete a operacao
input_ok = True #variavel de apoio para o while
while ( input_ok): #while infinito
    str = input('input string...: ') #pega strig do usuario
    if len(str) >= 30: #verifica se é maior igual a 30
        input_ok = False #se verdadeiro sai do while

#segunda fase do projeto - geracao da lista
lst = []  #cria uma lista vazia
for index in range(len(str)): #for usando o idx das posicoes da string informada
    lst.append(str[index]) #adiciona o caracter da posicao da string
    lst.append(len(str) - index) #adiciona o numero -1

#terceira parte geracao da tupla
tpl = tuple(lst) #converte a lista em uma tupla

#ultima parte do projeto imprime as saidas
print (str) #string informada
print (lst) #lista
print (tpl) #tupla
print (lst[:15]) #15 primeiras posicoes
print (tpl[-15:]) #15 ultimas posicoes

#bonus
print ('end application') #mensagem de fim da aplicacao
