import json
import re
import os

caminho_script = os.path.dirname(os.path.abspath(__file__))
caminho_ficheiro = os.path.join(caminho_script, 'dados.json')

with open(caminho_ficheiro, 'r', encoding='utf-8') as f:
    dados = json.load(f)

padrao_email = r'^\S+@\S+\.\S+$'

for registo in dados:
    email = registo['email']
    if re.match(padrao_email, email):
        print(f"O email {email} é válido.")
    else:
        print(f"O email {email} é inválido.")