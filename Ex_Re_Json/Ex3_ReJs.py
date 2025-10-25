import json
import os

caminho_script = os.path.dirname(os.path.abspath(__file__))
caminho_ficheiro = os.path.join(caminho_script, 'dados.json')

with open(caminho_ficheiro, 'r', encoding='utf-8') as f:
    dados = json.load(f)

print("Domínios extraídos:")
for registo in dados:
    site = registo['site']
    dominio = site.replace("https://", "").replace("http://", "").replace("www.", "")
    print(dominio)