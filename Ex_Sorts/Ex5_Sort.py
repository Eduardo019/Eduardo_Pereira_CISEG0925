# 5. Agrupar palavras pela letra inicial e ordenar cada grupo por ordem alfabética (A → Z)

lista_palavras = ["banana", "bola", "abacaxi", "arroz", "uva", "urso"]

grupos = {}

# Agrupa as palavras no dicionário
for palavra in lista_palavras:
    inicial = palavra[0]
    if inicial not in grupos:
        grupos[inicial] = []
    grupos[inicial].append(palavra)

# Ordena a lista de palavras dentro de cada grupo
for inicial in grupos:
    grupos[inicial].sort()

print(grupos)