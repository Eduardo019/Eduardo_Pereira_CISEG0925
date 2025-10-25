import json
import os

caminho_script = os.path.dirname(os.path.abspath(__file__))
caminho_input = os.path.join(caminho_script, 'dados.json')
caminho_output = os.path.join(caminho_script, 'nomes_emails.txt')

with open(caminho_input, 'r', encoding='utf-8') as f:
    dados = json.load(f)

with open(caminho_output, 'w', encoding='utf-8') as f_txt:
    for registo in dados:
        nome = registo['nome']
        email = registo['email']
        f_txt.write(f"Nome: {nome}, Email: {email}\n")

print(f"Ficheiro '{os.path.basename(caminho_output)}' criado com sucesso.")