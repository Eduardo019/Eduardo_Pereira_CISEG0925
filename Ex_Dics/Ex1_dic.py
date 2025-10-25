# Exercício 1: Criar um dicionário simples
alunos = {}
id_aluno = 1

while True:
    print("\n1- Inserir Aluno")
    print("2- Listar Alunos")
    print("0- Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        nome = input("Nome do aluno: ")
        idade = input("Idade do aluno: ")
        curso = input("Curso do aluno: ")
        alunos[id_aluno] = {'nome': nome, 'idade': idade, 'curso': curso}
        id_aluno += 1
        print("Aluno inserido com sucesso!")
    elif opcao == '2':
        if not alunos:
            print("Nenhum aluno registado.")
        else:
            for id_aluno, dados in alunos.items():
                print(f"\n--- Aluno {id_aluno} ---")
                print(f"nome: {dados['nome']}")
                print(f"idade: {dados['idade']}")
                print(f"curso: {dados['curso']}")
    elif opcao == '0':
        break
    else:
        print("Opção inválida.")