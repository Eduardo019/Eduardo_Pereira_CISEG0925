import re
import os

caminho_script = os.path.dirname(os.path.abspath(__file__))
caminho_input = os.path.join(caminho_script, 'registos.txt')
caminho_output = os.path.join(caminho_script, 'resumo.txt')

with open(caminho_input, 'r', encoding='utf-8') as f:
    linhas = f.readlines()

with open(caminho_output, 'w', encoding='utf-8') as f_out:
    for linha in linhas:
        nome = re.search(r'Nome: (.*?)\s\|', linha)
        nif = re.search(r'NIF: (\d{9})', linha)
        data = re.search(r'Data: (\d{2}/\d{2}/\d{4})', linha)
        cp = re.search(r'Código Postal: (\d{4}-\d{3})', linha)
        site = re.search(r'Site: (https?://[^\s|]+)', linha)

        if nome and nif and data and cp and site:
            site_limpo = site.group(1).replace("https://", "").replace("http://", "")
            linha_nova = f"{nome.group(1)} | {nif.group(1)} | {data.group(1)} | {cp.group(1)} | {site_limpo}\n"
            f_out.write(linha_nova)

print(f"Ficheiro '{os.path.basename(caminho_output)}' criado.")