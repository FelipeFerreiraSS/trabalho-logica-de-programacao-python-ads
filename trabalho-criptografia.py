frase = input("Digite a frase: ")
fraseArray = list(frase)

chave = int(input("Digite os dois ultimos numeros do seu RU: "))
chaveBit = format(chave, "08b")

tamanho = len(fraseArray)

listaAscii = []
for x in range(tamanho):
    listaAscii.append(ord(fraseArray[x])) #string para ascii

binario = []
for x in range(tamanho):
    binario.append(format(listaAscii[x], "08b")) #scii para binario

#Comparando a frase com a chave


#converteAscii = []
#for x in range(tamanho):
#    converteAscii.append(chr(listaAscii[x]))  #de ascii para string


print("Frase inicial:")
print(fraseArray)
print("---------")
print("Convertida em ascii")
print(listaAscii)
print("---------")
print("De ascii para binario")
print(binario)
#print("---------")
#print("Convertida de ascii")
#print(converteAscii)

