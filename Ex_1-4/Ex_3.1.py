listaNome = ["Dario Quental", "Dario Almeida", "Bruno Carvalho"]

for i in range(len(listaNome)-1):
    for j in range(i + 1, len(listaNome)):
        if listaNome[i] < listaNome[j]:
            listaNome[i], listaNome[j] = listaNome[j], listaNome[i]