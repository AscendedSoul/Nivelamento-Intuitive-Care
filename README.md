 Teste de Nivelamento - Intuitive Care

Este projeto foi desenvolvido como parte do teste de nivelamento do processo seletivo para a vaga de estágio na Intuitive Care. Ele implementa funcionalidades como extração de dados de websites (web scraping), formatação desses dados para importação, desenvolvimento de queries analíticas em MySQL e criação de um website para consultas aos dados extraídos.

 Tecnologias Utilizadas:

📥 Web Scraping (Python - main.py)

requests → Download de PDFs do site.

zipfile → Compactação dos PDFs em um arquivo .ZIP.

pdfplumber → Extração de tabelas de dados dos PDFs.

csv → Formatação de arquivos para análise.

🗄️ Banco de Dados e SQL

MySQL → Armazenamento e consultas aos dados.

Docker → Gerenciamento do ambiente de banco de dados.

🌐 Servidor Backend (Python - server.py)

Flask → Criação da API para busca de operadoras por CNPJ.

pandas → Manipulação de dados do CSV.

fuzzywuzzy → Busca de CNPJs similares com fuzzy matching.

🎨 Interface Web

Vue.js → Construção de um frontend interativo.

Axios → Consumo da API Flask.

⚙️ Funcionalidades do Projeto


📥 Web Scraping e Processamento de Dados (Itens 1 e 2 do teste)

Arquivo: main.py

O projeto realiza web scraping para baixar arquivos PDF de URLs pré-definidas, armazenando-os na pasta pdfs/. Posteriormente, esses arquivos são compactados em um .ZIP na pasta Arquivos Compactados/. Os dados extraídos dos PDFs são processados com pdfplumber, convertidos em tabelas e salvos no formato CSV dentro da pasta CSV/. Além disso, algumas padronizações são aplicadas para garantir a consistência dos dados. O arquivo CSV final também é compactado para facilitar o compartilhamento.

Arquivo: Conversor.py

🗄️ Operações com Banco de Dados MySQL (Item 3 do teste)

Essa etapa é responsável por importar e elaborar queries SQL para manipulação e análise dos dados extraídos.

Operações com SQL:

Query Cadastros.sql → Cria a tabela operadoras_saude para armazenar os dados das operadoras contidos no arquivo Relatorio_cadop.csv.

Query Contabilidade2023.sql e Query Contabilidade2024.sql → Estruturam tabelas para armazenar corretamente os dados financeiros trimestrais de cada ano.

Query Import cadastros.sql → Importa os dados do .csv para a tabela operadoras_saude.

Query import contabil.sql → Importa os relatórios trimestrais para as tabelas do banco de dados.

Query Primeira pergunta.sql → Retorna a resposta da primeira questão do item 3.5 do teste.

Query Segunda pergunta.sql → Retorna a resposta da segunda questão do item 3.5 do teste.


🌐 Servidor Flask e Interface Web Vue.js (Item 4 do teste)

Arquivo: server.py

O backend foi desenvolvido com Flask e expõe uma API REST para consulta de operadoras de saúde a partir do CNPJ. O servidor:

Carrega um arquivo CSV contendo os dados das operadoras.

Aplica validações e padronizações nos dados.

Utiliza fuzzy matching (via fuzzywuzzy) para encontrar CNPJs similares.

Disponibiliza a rota /buscar, que retorna os resultados mais relevantes no formato JSON.

 Interface Web Vue.js

O frontend foi desenvolvido com Vue.js e permite aos usuários consultar operadoras por meio do CNPJ. Ele:

Possui um campo de entrada para digitação do CNPJ.

Faz requisições à API Flask via Axios.

Exibe os resultados encontrados de forma intuitiva.

Apresenta mensagens de erro para entradas inválidas ou resultados não encontrados.

*OBS: A file de coleção do Postman é: Teste GET operadoras_saude.postman_collection.json.