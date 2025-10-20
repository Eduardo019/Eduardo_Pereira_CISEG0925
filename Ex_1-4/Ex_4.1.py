############################################################################
# Exercicio 4.1 Atualiza o codigo anterior para incluir letras pequenas e com acentos.
# Em que E maior , e menor ou é com acento valem o mesmo, e as restantes letras igual.
# Incluir todas as acentuações portuguesas a valer o mesmo que a letra normal tal como explicado em cima.
# EX: lista=[" Eu Gosto é do verão"]
lista=["Eu Gosto é do verão"]
listaNome = lista[0].split()
print(listaNome)
def chave_ordenacao(palavra):
    # Define uma chave de ordenação personalizada
    tabela_ordenacao = str.maketrans(
        "áàâãäéèêëíìîïóòôõöúùûüçÁÀÂÃÄÉÈÊËÍÌÎÏÓÒÔÕÖÚÙÛÜÇ",
        "aaaaaeeeeiiiiooooouuuucAAAAAEEEEIIIIOOOOOUUUUC"
    )
    return palavra.translate(tabela_ordenacao).lower()
for i in range(len(listaNome)-1):
    for j in range(i + 1, len(listaNome)):
        if chave_ordenacao(listaNome[i]) < chave_ordenacao(listaNome[j]):
            listaNome[i], listaNome[j] = listaNome[j], listaNome[i]
print(listaNome)
print("".join(listaNome))  # Junta as palavras de volta em uma única string
