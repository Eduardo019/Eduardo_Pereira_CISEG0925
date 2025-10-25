import re
import os

caminho_script = os.path.dirname(os.path.abspath(__file__))
caminho_ficheiro = os.path.join(caminho_script, 'registos.txt')

with open(caminho_ficheiro, 'r', encoding='utf-8') as f:
    conteudo = f.read()

# Procura por URLs que terminem em .pt
sites_pt = re.findall(r'https?://[^\s|]+\.pt', conteudo)
print("Sites terminados em .pt:", sites_pt)