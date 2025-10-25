import re
import os

caminho_script = os.path.dirname(os.path.abspath(__file__))
caminho_ficheiro = os.path.join(caminho_script, 'registos.txt')

with open(caminho_ficheiro, 'r', encoding='utf-8') as f:
    conteudo = f.read()

datas = re.findall(r'\b\d{2}/\d{2}/\d{4}\b', conteudo)
print("Datas encontradas:", datas)