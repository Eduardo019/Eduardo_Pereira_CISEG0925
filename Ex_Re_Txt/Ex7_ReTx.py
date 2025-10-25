import re
import os

caminho_script = os.path.dirname(os.path.abspath(__file__))
caminho_ficheiro = os.path.join(caminho_script, 'registos.txt')

with open(caminho_ficheiro, 'r', encoding='utf-8') as f:
    conteudo = f.read()

nifs = re.findall(r'\b\d{9}\b', conteudo)
print("NIFs encontrados:", nifs)