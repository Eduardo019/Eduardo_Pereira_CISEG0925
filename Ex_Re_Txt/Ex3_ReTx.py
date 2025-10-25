import re
import os

caminho_script = os.path.dirname(os.path.abspath(__file__))
caminho_ficheiro = os.path.join(caminho_script, 'dados.txt')

with open(caminho_ficheiro, 'r', encoding='utf-8') as f:
    conteudo = f.read()

telemoveis = re.findall(r'\d{9}|\d{3}[-\s]\d{3}[-\s]\d{3}', conteudo)
print("Telemóveis encontrados:", telemoveis)