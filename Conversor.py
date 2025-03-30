import csv

#Código necessário para corrigir a vírgula pelo ponto nos números float(3.1) para utilização dos dados no MySQL:

entrada_csv = ["CSV/Financeiro/1T2024.csv",
               "CSV/Financeiro/2T2024.csv",
               "CSV/Financeiro/3T2024.csv",
               "CSV/Financeiro/4T2024.csv",
               "CSV/Financeiro/1T2024.csv",
               "CSV/Financeiro/2T2024.csv",
               "CSV/Financeiro/3T2024.csv",
               "CSV/Financeiro/4T2024.csv"
]

saida_csv = ["CSV/Financeiro/1T2024_convertido.csv",
             "CSV/Financeiro/2T2024_convertido.csv",
             "CSV/Financeiro/3T2024_convertido.csv",
             "CSV/Financeiro/4T2024_convertido.csv",
             "CSV/Financeiro/1T2023_convertido.csv",
             "CSV/Financeiro/2T2023_convertido.csv",
             "CSV/Financeiro/3T2023_convertido.csv",
             "CSV/Financeiro/4T2023_convertido.csv"
]

for i in range(0, 8, 1):
    with open(entrada_csv[i], "r", encoding="utf-8") as entrada, \
         open(saida_csv[i], "w", encoding="utf=8", newline="") as saida:
            leitor = csv.reader(entrada, delimiter=";")
            escritor = csv.writer(saida, delimiter=";")

            for linha in leitor:
                 nova_linha = [col.replace(",", ".") if col.replace(",", "").replace(".","").isdigit() else col for col in linha]
                 escritor.writerow(nova_linha)
    print(f"Arquivo formatado: {entrada_csv[i]} para {saida_csv[i]}.")