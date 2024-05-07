import qrcode
import csv
import os
import json
from pathlib import Path



def ler_csv(arquivo):
    dados = []
    with open(arquivo, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        
        # Ler o cabeçalho
        header = next(reader)

        # Ler as duas primeiras linhas de dados
        for i in range(398):
            row = next(reader, None)
            if row is not None:
                nome = row[0]
                nome_img = row[2]
                dias_almoco = [dia.strip() for dia in row[1].split(',')]
                aluno_dados = json.dumps({'nome': nome, 'comida': dias_almoco})
                dados.append(aluno_dados)

                imagem = qrcode.make(aluno_dados)

                nome = row[0].replace(' ', '_')
                nome_img = row[2].replace('/', '_').split('.')[0][:2]
                
                pasta = f'qrcode/img/{nome_img}'
                Path(pasta).mkdir(parents=True, exist_ok=True)


                caminho_imagem = os.path.join(f'qrcode/img/{nome_img}', f"{nome_img}_{nome}.png")

                imagem.save(caminho_imagem)

    return dados

# Teste
arquivo_csv = 'C:/Users/Suporte/Documents/qrcode-exe-main/assets/Lista.csv'
dados_formatados = ler_csv(arquivo_csv)
print(dados_formatados)

