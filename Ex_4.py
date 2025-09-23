''' 
    Exercicio 4 Ordena as Letras de Z-A de em uma lista com uma unica string. Exemplo: lista=[" EU GOSTO E DO VERAO"]
'''

lista=["EU GOSTO E DO VERAO"]
listaNome = lista[0].split()  # Divide a string em palavras
print(listaNome)
for i in range(len(listaNome)-1):
    for j in range(i + 1, len(listaNome)):
        if listaNome[i] < listaNome[j]:
            listaNome[i], listaNome[j] = listaNome[j], listaNome[i]
print(listaNome)
print("".join(listaNome))
