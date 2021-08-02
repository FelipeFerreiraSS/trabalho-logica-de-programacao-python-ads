frase = input("Digite a frase")

fraseArray = list(frase)

tamanho = len(fraseArray)

listaAscii = []
for x in range(tamanho):
    listaAscii.append(ord(fraseArray[x])) #string para ascii

binario = []
for i in range(tamanho):
    binario.append(format(listaAscii[i], "08b")) #scii para binario

converteAscii = []
for x in range(tamanho):
    converteAscii.append(chr(listaAscii[x]))  #de ascii para string


print("Frase inicial:")
print(fraseArray)
print("---------")
print("Convertida em ascii")
print(listaAscii)
print("---------")
print("De ascii para binario")
print(binario)
print("---------")
print("Convertida de ascii")
print(converteAscii)

temp = "{0:b}".format(722)

print(temp)


