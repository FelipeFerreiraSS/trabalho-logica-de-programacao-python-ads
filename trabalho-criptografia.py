frase = input("Digite a frase")

fraseArray = list(frase)

tamanho = len(fraseArray)

listaAscii = []

for x in range(tamanho):
    listaAscii.append(ord(fraseArray[x]))

converteAscii = []

for x in range(tamanho):
    converteAscii.append(chr(listaAscii[x]))


print("Frase inicial:")
print(fraseArray)
print("---------")
print("Convertida em ascii")
print(listaAscii)
print("---------")
print("Convertida de ascii")
print(converteAscii)


