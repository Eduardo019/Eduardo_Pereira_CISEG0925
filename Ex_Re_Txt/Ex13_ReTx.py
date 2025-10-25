import re
from datetime import datetime
import os

caminho_script = os.path.dirname(os.path.abspath(__file__))
caminho_ficheiro = os.path.join(caminho_script, 'registos.txt')

with open(caminho_ficheiro, 'r', encoding='utf-8') as f:
    linhas = f.readlines()

print("Registos com data anterior a 2025:")
for linha in linhas:
    match_data = re.search(r'\b(\d{2}/\d{2}/\d{4})\b', linha)
    if match_data:
        data_str = match_data.group(1)
        data_obj = datetime.strptime(data_str, '%d/%m/%Y')
        if data_obj.year < 2025:
            print(linha.strip())