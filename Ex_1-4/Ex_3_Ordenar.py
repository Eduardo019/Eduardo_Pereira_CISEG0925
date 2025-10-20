listaNome = ["Dario Quental", "Dario Almeida", "Bruno Carvalho"]

n = len(listaNome)

for passagem in range(n - 1):
    
    for i in range(n - 1 - passagem):
        
        if listaNome[i] > listaNome[i+1]:
            
            listaNome[i], listaNome[i+1] = listaNome[i+1], listaNome[i]

print("Lista Ordenada:", listaNome)