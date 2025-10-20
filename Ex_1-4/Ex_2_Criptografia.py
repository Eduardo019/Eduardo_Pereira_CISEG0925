def calcular_chave_numerica(chave): # Soma os valores ASCII
    soma = 0
    for letra in chave:
        soma += ord(letra)
    return soma

def criptografar(mensagem, chave):
    chave_numerica = calcular_chave_numerica(chave)
    dados_criptografados = []

    for char in mensagem:
        codigo = ord(char)
        
        # Se for um caractere "imprimível", usa rotação.
        if 32 <= codigo <= 126:
            posicao = codigo - 32
            nova_posicao = (posicao + chave_numerica) % 95
            novo_codigo = nova_posicao + 32
            # Guarda o código e a informação de que foi rotacionado (True)
            dados_criptografados.append((novo_codigo, True))
        else:
            # Para outros caracteres, apenas soma.
            novo_codigo = codigo + chave_numerica
            # Guarda o código e a informação de que não foi rotacionado (False)
            dados_criptografados.append((novo_codigo, False))
            
    return dados_criptografados

def descriptografar(dados, chave):
    chave_numerica = calcular_chave_numerica(chave)
    mensagem_final = ""

    for codigo, foi_rotacionado in dados:
        if foi_rotacionado: # Desfaz a rotação
            posicao = codigo - 32
            posicao_original = (posicao - chave_numerica) % 95
            codigo_original = posicao_original + 32
            mensagem_final += chr(codigo_original)
        else: # Desfaz a soma simples
            codigo_original = codigo - chave_numerica
            mensagem_final += chr(codigo_original)

    return mensagem_final

# MENU PRINCIPAL
mensagens_guardadas = []

while True:
    print("\n--- Menu ---")
    print("1. Criptografar")
    print("2. Descriptografar")
    print("3. Listar mensagens")
    print("4. Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        mensagem = input("Mensagem para criptografar: ")
        
        while True:
            chave = input("Chave de criptografia: ")
            if chave:
                break
            print("A chave não pode ser vazia!")
            
        dados = criptografar(mensagem, chave)
        mensagens_guardadas.append((dados, chave))
        
        texto_cifrado = ""
        for codigo, _ in dados:
            texto_cifrado += chr(codigo)

        print("\nMensagem criptografada com sucesso!")
        print(f"Texto cifrado: {texto_cifrado}")

    elif opcao == '2':
        if not mensagens_guardadas:
            print("\nNenhuma mensagem para descriptografar.")
            continue
        
        print("\nEscolha a mensagem para descriptografar:")
        for i, (dados, _) in enumerate(mensagens_guardadas):
            texto_cifrado = "".join([chr(c) for c, _ in dados])
            print(f"{i + 1}: {texto_cifrado[:50]}")

        try:
            escolha = int(input("Número da mensagem: ")) - 1
            dados_para_descriptografar, chave_original = mensagens_guardadas[escolha]
            
            chave_teste = input("Introduza a chave correta: ")
            
            if chave_teste == chave_original:
                mensagem_original = descriptografar(dados_para_descriptografar, chave_teste)
                print("\nMensagem original:", mensagem_original)
            else:
                print("\nChave incorreta!")
        except:
            print("Escolha inválida.")

    elif opcao == '3':
        if not mensagens_guardadas:
            print("\nNenhuma mensagem guardada.")
        else:
            print("\n--- Mensagens Guardadas ---")
            for i, (dados, chave) in enumerate(mensagens_guardadas):
                texto_cifrado = "".join([chr(c) for c, _ in dados])
                print(f"Mensagem {i + 1}: {texto_cifrado}")

    elif opcao == '4':
        print("Até logo!")
        break

    else:
        print("Opção inválida. Tente novamente.")