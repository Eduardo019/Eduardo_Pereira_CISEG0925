def validar_nome_simples():
    while True:
        nome = input("Por favor, introduza o seu nome completo: ")
        valido = True
        encontrou_espaco = False
        
        for i, char in enumerate(nome):
            ascii_val = ord(char)

            if i == 0:  # Primeira letra do nome
                if not (65 <= ascii_val <= 90):  # Verifica se é uma letra maiúscula (A-Z)
                    print("Nome inválido: A primeira letra do nome deve ser maiúscula.")
                    valido = False
                    return
            elif char == ' ':
                encontrou_espaco = True
            elif encontrou_espaco and (i > 0 and nome[i-1] == ' '):  # Primeira letra depois de um espaço
                if not (65 <= ascii_val <= 90):  # Verifica se é uma letra maiúscula (A-Z)
                    print("Nome inválido: A primeira letra depois do espaço deve ser maiúscula.")
                    valido = False
                    return
                encontrou_espaco = False # Para o próximo potencial espaço
            else: # Outras letras (minúsculas permitidas)
                if not (97 <= ascii_val <= 122) and not (char == ' '): # Verifica se é uma letra minúscula (a-z) ou um espaço
                    print("Nome inválido: contém caracteres não permitidos.")
                    valido = False
                    return
        if valido:
            print("Nome válido!")
        else:
            break

validar_nome_simples()