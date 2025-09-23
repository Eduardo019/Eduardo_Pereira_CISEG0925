listaNome = ["Dario Quental", "Dario Almeida", "Bruno Carvalho"]

n = len(listaNome)

# O primeiro loop controla o número de "passagens" pela lista.
for passagem in range(n - 1):
    
    # O segundo loop percorre a lista para comparar os elementos adjacentes.
    # A cada passagem, o maior elemento "borbulha" para o final,
    # então podemos diminuir o alcance deste loop (a otimização "- passagem").
    for i in range(n - 1 - passagem):
        
        # Compara o elemento atual com o próximo.
        # Python já sabe comparar strings em ordem alfabética.
        if listaNome[i] > listaNome[i+1]:
            
            # Se estiverem fora de ordem, troca-os de posição.
            # Esta é a forma padrão e mais eficiente de fazer uma troca em Python.
            listaNome[i], listaNome[i+1] = listaNome[i+1], listaNome[i]

print("Lista Ordenada:", listaNome)