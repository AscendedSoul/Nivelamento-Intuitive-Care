from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
from fuzzywuzzy import process

app = Flask(__name__)
CORS(app)

CSV_PATH = "CSV/Dados Cadastrais/Relatorio_cadop.csv"

#Carregar CSV com verificação
try:
    df = pd.read_csv(CSV_PATH, sep=";", dtype=str, encoding="utf-8")
    df = df.fillna("")
    df.rename(columns=lambda x: x.strip(), inplace=True)
except Exception as e:
    print(f"Erro ao carregar CSV: {e}")
    df = pd.DataFrame()

if not df.empty and "CNPJ" in df.columns:
    df["CNPJ"] = df["CNPJ"].str.strip()
else:
    print(" CSV não contém a coluna CNPJ.")
    df["CNPJ"] = ""

#Função Buscar:
def buscar_operadora(cnpj):
    if df.empty or "CNPJ" not in df.columns:
        return []

    cnpj = cnpj.strip()
    resultados = process.extract(cnpj, df["CNPJ"], limit=5)

    operadoras_encontradas = [df.iloc[idx].to_dict() for _, score, idx in resultados if score > 80]  # Maior precisão

    return operadoras_encontradas

#Rota da API
@app.route("/buscar", methods=["GET"])
def buscar():
    cnpj = request.args.get("cnpj", "").strip()

    if not cnpj:
        return jsonify({"erro": "É necessário fornecer um CNPJ para busca."}), 400
    
    resultados = buscar_operadora(cnpj)
    return jsonify(resultados)

if __name__ == "__main__":
    app.run(debug=True)
