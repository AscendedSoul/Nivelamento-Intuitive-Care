LOAD DATA INFILE 'CSV/Financeiro/4T2024_convertido.csv'
INTO TABLE contabilidade2024
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

-- Esse comando é utilizado para importar cada trimestre dos ultimos 2 anos.