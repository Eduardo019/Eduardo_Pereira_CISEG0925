# Exercício 5: Contar letras numa palavra
palavra = input("Introduza uma palavra: ")

contagem = {}
for letra in palavra:
    if letra in contagem:
        contagem[letra] = contagem[letra] + 1
    else:
        contagem[letra] = 1

print(contagem)