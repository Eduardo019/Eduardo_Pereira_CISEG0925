# Exercício 10: Contar palavras numa frase
frase = input("Introduza uma frase: ")

# Divide a frase numa lista de palavras
palavras = frase.split()

contagem = {}
for palavra in palavras:
    if palavra in contagem:
        contagem[palavra] += 1
    else:
        contagem[palavra] = 1

print(contagem)