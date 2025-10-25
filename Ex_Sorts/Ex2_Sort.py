# 2. Ordenar uma lista de palavras por ordem alfabética inversa (Z → A), ignorando maiúsculas/minúsculas

lista_palavras = ["Python", "inteligência", "Aprender", "dados", "Rede"]

# key=str.lower trata todas as palavras como se estivessem em minúsculas para a comparação
# reverse=True inverte a ordem da ordenação
resultado = sorted(lista_palavras, key=str.lower, reverse=True)

print(resultado)