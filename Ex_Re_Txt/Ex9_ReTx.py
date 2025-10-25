import re
import os

caminho_script = os.path.dirname(os.path.abspath(__file__))
caminho_ficheiro = os.path.join(caminho_script, 'registos.txt')

with open(caminho_ficheiro, 'r', encoding='utf-8') as f:
    conteudo = f.read()

codigos_postais = re.findall(r'\b\d{4}-\d{3}\b', conteudo)
print("Códigos Postais encontrados:", codigos_postais)