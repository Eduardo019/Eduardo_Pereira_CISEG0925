# Exercício 8: Juntar dois dicionários
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}

d_junto = d1.copy()  # Copia d1 para não o alterar
d_junto.update(d2)   # Adiciona os itens de d2

print(d_junto)