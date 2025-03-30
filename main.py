import requests
import os
import zipfile
import pdfplumber
#import tabula   
import csv

#1. Web Scraping
link_pdf = [
    "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf",
    "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_II_DUT_2021_RN_465.2021_RN628.2025_RN629.2025.pdf"
]

pasta = 'pdfs'
os.makedirs(pasta, exist_ok=True)

pasta2 = 'Dados Cadastrais'
os.makedirs(pasta2, exist_ok=True)

pasta3 = 'Arquivos Compactados'
os.makedirs(pasta3, exist_ok=True)

pasta_CSV = 'CSV'
os.makedirs(pasta_CSV, exist_ok=True)

arquivos_pdf = []
for i, url in enumerate(link_pdf):
    nome_pdf = os.path.join(pasta, f"anexo_{i+1}.pdf")
    response = requests.get(url, stream = True)

    if response.status_code == 200:
        with open(nome_pdf, "wb") as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)
        arquivos_pdf.append(nome_pdf)
        print(f"Baixado: {nome_pdf}")

path_zip = "Arquivos Compactados/pdfs_compactados.zip"
with zipfile.ZipFile(path_zip, "w") as zipf:
    for pdf in arquivos_pdf:
        zipf.write(pdf, os.path.basename(pdf))
        print(f"Adicionado ao ZIP: {pdf}")

print(f"Todos os PDFs foram compactados em {path_zip}")

#2 Transformação de dados
tabela_extraida = []

substituicoes = {
    "OD":"SEG.ODONTOLÓGICA",
    "AMB":"SEG.AMBULATORIAL"
}

with pdfplumber.open("pdfs/anexo_1.pdf") as pdf:
    for pagina in pdf.pages:
        tabela = pagina.extract_table()
        if tabela:
                tabela_extraida.extend(tabela)
                tabela_corrigida = [[substituicoes.get(dado, dado) if dado else "" for dado in linha] for linha in tabela_extraida]
#                print(tabela_corrigida)

with open("CSV/tabela_Anexo1.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(tabela_corrigida)
print("tabela csv gerada.")

path_zip2 = "Arquivos Compactados/Teste_Pedro_Yan.zip"
arquivo_csv = "CSV/tabela_Anexo1.csv"
with zipfile.ZipFile(path_zip2, "w", zipfile.ZIP_DEFLATED) as zipf:
    for csv in arquivo_csv:
        zipf.write(arquivo_csv, os.path.basename(arquivo_csv))
print(f"Arquivo ZIP {path_zip2} criado.")
