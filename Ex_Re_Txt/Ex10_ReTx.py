import re
import os

caminho_script = os.path.dirname(os.path.abspath(__file__))
caminho_ficheiro = os.path.join(caminho_script, 'registos.txt')

with open(caminho_ficheiro, 'r', encoding='utf-8') as f:
    conteudo = f.read()

sites = re.findall(r'https?://[^\s|]+', conteudo)
dominios = []
for site in sites:
    dominio = site.replace("https://", "").replace("http://", "").replace("www.", "")
    dominios.append(dominio)

print("Domínios:", dominios)