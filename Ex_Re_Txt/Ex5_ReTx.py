import re
import os

caminho_script = os.path.dirname(os.path.abspath(__file__))
caminho_input = os.path.join(caminho_script, 'dados.txt')
caminho_output = os.path.join(caminho_script, 'extraidos.txt')

with open(caminho_input, 'r', encoding='utf-8') as f:
    linhas = f.readlines()

with open(caminho_output, 'w', encoding='utf-8') as f_out:
    for linha in linhas:
        nome = re.search(r'Nome: (.*?)(?=,)', linha)
        email = re.search(r'Email: (\S+@\S+\.\S+)', linha)
        tel = re.search(r'Telemóvel: ([\d\s-]+)', linha)

        if nome and email and tel:
            linha_nova = f"{nome.group(1).strip()} | {email.group(1).strip()} | {tel.group(1).strip()}\n"
            f_out.write(linha_nova)

print(f"Ficheiro '{os.path.basename(caminho_output)}' criado com sucesso.")