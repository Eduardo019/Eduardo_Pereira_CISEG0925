import json
import re
import os

caminho_script = os.path.dirname(os.path.abspath(__file__))
caminho_input = os.path.join(caminho_script, 'dados.json')
caminho_output = os.path.join(caminho_script, 'dados_validos.json')

with open(caminho_input, 'r', encoding='utf-8') as f:
    dados = json.load(f)

padrao_email = r'^\S+@\S+\.\S+$'
padrao_nif = r'^[123568]\d{8}$'
registos_validos = []

for registo in dados:
    email_valido = re.match(padrao_email, registo['email'])
    nif_valido = re.match(padrao_nif, registo['nif'])
    apenas_digitos = re.sub(r'\D', '', registo['telemovel'])
    telemovel_valido = len(apenas_digitos) == 9

    if email_valido and nif_valido and telemovel_valido:
        registos_validos.append(registo)

with open(caminho_output, 'w', encoding='utf-8') as f:
    json.dump(registos_validos, f, indent=2)

print(f"Ficheiro '{os.path.basename(caminho_output)}' criado com sucesso.")