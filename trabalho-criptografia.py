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

cifra = []
#Comparando a frase com a chave
for x in range(tamanho):
    for i in range(8):
        if (binario[x][i] == chaveBit[i]):
            cifra.append(0)
        else:
            cifra.append(1)


#converteAscii = []
#for x in range(tamanho):
#    converteAscii.append(chr(listaAscii[x]))  #de ascii para string


print("Frase inicial:")
print(fraseArray)
print("---------")
print("chaveBit")
print(chaveBit)
print("---------")
print("De ascii para binario")
print(binario)
print("---------")
print("Cifra")
print(cifra)

