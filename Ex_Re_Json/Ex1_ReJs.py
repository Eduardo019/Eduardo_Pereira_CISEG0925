import json
import os

# Constrói o caminho para o ficheiro 'dados.json' que está na mesma pasta do script
caminho_script = os.path.dirname(os.path.abspath(__file__))
caminho_ficheiro = os.path.join(caminho_script, 'dados.json')

with open(caminho_ficheiro, 'r', encoding='utf-8') as f:
    dados = json.load(f)

print(dados)