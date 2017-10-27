print('Bom dia')

a = 0



while (a == 0):
    frase = input("Digite a string...:")
    if len(frase) >= 5:
        a =1
    else:
        print('A Frase não atente os requisitos')
        a= 0

t = len(frase)
lista = []
for letra in frase:
    lista.append('%c' % letra)

    lista.append('%d' % t)
    t = t - 1

for letras in lista:
    print('letra é: %c' % letras)
