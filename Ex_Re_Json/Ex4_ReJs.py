import json
import re
import os

caminho_script = os.path.dirname(os.path.abspath(__file__))
caminho_ficheiro = os.path.join(caminho_script, 'dados.json')

with open(caminho_ficheiro, 'r', encoding='utf-8') as f:
    dados = json.load(f)

padrao_nif = r'^[123568]\d{8}$'

for registo in dados:
    nif = registo['nif']
    if re.match(padrao_nif, nif):
        print(f"O NIF {nif} é válido.")
    else:
        print(f"O NIF {nif} é inválido.")