import re
import os

caminho_script = os.path.dirname(os.path.abspath(__file__))
caminho_ficheiro = os.path.join(caminho_script, 'registos.txt')

with open(caminho_ficheiro, 'r', encoding='utf-8') as f:
    conteudo = f.read()

nifs = re.findall(r'\b\d{9}\b', conteudo)
digitos_validos = ['1', '2', '3', '5', '6', '8']
nifs_validos = []

for nif in nifs:
    if nif[0] in digitos_validos:
        nifs_validos.append(nif)

print("NIFs com primeiro dígito válido:", nifs_validos)