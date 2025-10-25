# Exercício 3: Criar um dicionário vazio chamado produto

produto = {}
produto['nome'] = "Telemóvel"
produto['preço'] = 1500
produto['stock'] = 30
print("Dicionário após adições:", produto)

# Remove a chave stock do dicionário.
del produto['stock']

print("Dicionário final:", produto)