# 4. Ordenar uma lista de palavras pela quantidade de letras minúsculas

lista_palavras = ["PYthon", "banana", "CÓDIGO", "intELIGENTE", "dados"]

def contar_letras_minusculas(palavra):
    contador = 0
    for letra in palavra:
        if 'a' <= letra <= 'z':
            contador = contador + 1
    return contador

# Usa a função como "chave" para a ordenação
resultado = sorted(lista_palavras, key=contar_letras_minusculas)

print(resultado)