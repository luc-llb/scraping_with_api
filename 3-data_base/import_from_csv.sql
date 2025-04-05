-- Import datas to the operadoras_de_plano_de_saude_ativas table
LOAD DATA INFILE 'files/Relatorio_cadop.csv'
INTO TABLE operadoras_de_plano_de_saude_ativas
FIELDS TERMINATED BY ';' ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@registro_ans, @cnpj, @razao_social, @nome_fantasia, @modalidade, @logradouro, @numero, @complemento, @bairro, @cidade, @uf, @cep, @ddd, @telefone, @fax, @endereco_eletronico, @representante, @cargo_representante, @regiao_de_comercializacao, @_data_registro_ans)
SET
    registro_ans = CAST(@registro_ans AS UNSIGNED),
    cnpj = @cnpj,
    razao_social = @razao_social,
    nome_fantasia = @nome_fantasia,
    modalidade = @modalidade,
    logradouro = @logradouro,
    numero = @numero,
    complemento = @complemento,
    bairro = @bairro,
    cidade = @cidade,
    uf = @uf,
    cep = @cep,
    ddd = @ddd,
    telefone = @telefone,
    fax = @fax,
    endereco_eletronico = @endereco_eletronico,
    representante = @representante,
    cargo_representante = @cargo_representante,
    regiao_de_comercializacao = @regiao_de_comercializacao,
    data_registro_ans = STR_TO_DATE(@_data_registro_ans, '%Y-%m-%d');

-- Import datas to the demonstracoes_contabeis table

-- Remove the foreign key constraint before importing data (as it may not exist in the CSV files)
ALTER TABLE demonstracoes_contabeis DROP FOREIGN KEY ct_demonstracoes_contabeis_reg_ans;

-- 2023 Archives
LOAD DATA INFILE 'files/1T2023.csv'
INTO TABLE demonstracoes_contabeis
FIELDS TERMINATED BY ';' ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@_data, @reg_ans, @cd_conta_contabil, @descricao, @vl_saldo_inicial, @vl_saldo_final) 
SET
    _data = STR_TO_DATE(@_data, '%Y-%m-%d'),
    reg_ans = CAST(@reg_ans AS UNSIGNED),
    cd_conta_contabil = CAST(@cd_conta_contabil AS UNSIGNED),
    descricao = TRIM(@descricao),
    vl_saldo_inicial = CAST(REPLACE(REGEXP_REPLACE(@vl_saldo_inicial, '[^0-9,.-]', ''), ',', '.') AS DECIMAL(10,2)),
    vl_saldo_final = CAST(REPLACE(REGEXP_REPLACE(@vl_saldo_final, '[^0-9,.-]', ''), ',', '.') AS DECIMAL(10,2));

LOAD DATA INFILE 'files/2t2023.csv'
INTO TABLE demonstracoes_contabeis
FIELDS TERMINATED BY ';' ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@_data, @reg_ans, @cd_conta_contabil, @descricao, @vl_saldo_inicial, @vl_saldo_final) 
SET
    _data = STR_TO_DATE(@_data, '%Y-%m-%d'),
    reg_ans = CAST(@reg_ans AS UNSIGNED),
    cd_conta_contabil = CAST(@cd_conta_contabil AS UNSIGNED),
    descricao = TRIM(@descricao),
    vl_saldo_inicial = CAST(REPLACE(REGEXP_REPLACE(@vl_saldo_inicial, '[^0-9,.-]', ''), ',', '.') AS DECIMAL(10,2)),
    vl_saldo_final = CAST(REPLACE(REGEXP_REPLACE(@vl_saldo_final, '[^0-9,.-]', ''), ',', '.') AS DECIMAL(10,2));

LOAD DATA INFILE 'files/3T2023.csv'
INTO TABLE demonstracoes_contabeis
FIELDS TERMINATED BY ';' ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@_data, @reg_ans, @cd_conta_contabil, @descricao, @vl_saldo_inicial, @vl_saldo_final) 
SET
    _data = STR_TO_DATE(@_data, '%Y-%m-%d'),
    reg_ans = CAST(@reg_ans AS UNSIGNED),
    cd_conta_contabil = CAST(@cd_conta_contabil AS UNSIGNED),
    descricao = TRIM(@descricao),
    vl_saldo_inicial = CAST(REPLACE(REGEXP_REPLACE(@vl_saldo_inicial, '[^0-9,.-]', ''), ',', '.') AS DECIMAL(10,2)),
    vl_saldo_final = CAST(REPLACE(REGEXP_REPLACE(@vl_saldo_final, '[^0-9,.-]', ''), ',', '.') AS DECIMAL(10,2));

LOAD DATA INFILE 'files/4T2023.csv'
INTO TABLE demonstracoes_contabeis
FIELDS TERMINATED BY ';' ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@_data, @reg_ans, @cd_conta_contabil, @descricao, @vl_saldo_inicial, @vl_saldo_final) 
SET
    _data = STR_TO_DATE(@_data, '%d/%m/%Y'),
    reg_ans = CAST(@reg_ans AS UNSIGNED),
    cd_conta_contabil = CAST(@cd_conta_contabil AS UNSIGNED),
    descricao = TRIM(@descricao),
    vl_saldo_inicial = CAST(REPLACE(REGEXP_REPLACE(@vl_saldo_inicial, '[^0-9,.-]', ''), ',', '.') AS DECIMAL(10,2)),
    vl_saldo_final = CAST(REPLACE(REGEXP_REPLACE(@vl_saldo_final, '[^0-9,.-]', ''), ',', '.') AS DECIMAL(10,2));

-- 2024 Archives
LOAD DATA INFILE 'files/1T2024.csv'
INTO TABLE demonstracoes_contabeis
FIELDS TERMINATED BY ';' ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@_data, @reg_ans, @cd_conta_contabil, @descricao, @vl_saldo_inicial, @vl_saldo_final) 
SET
    _data = STR_TO_DATE(@_data, '%Y-%m-%d'),
    reg_ans = CAST(@reg_ans AS UNSIGNED),
    cd_conta_contabil = CAST(@cd_conta_contabil AS UNSIGNED),
   descricao = TRIM(@descricao),
    vl_saldo_inicial = CAST(REPLACE(REGEXP_REPLACE(@vl_saldo_inicial, '[^0-9,.-]', ''), ',', '.') AS DECIMAL(10,2)),
    vl_saldo_final = CAST(REPLACE(REGEXP_REPLACE(@vl_saldo_final, '[^0-9,.-]', ''), ',', '.') AS DECIMAL(10,2));

LOAD DATA INFILE 'files/2T2024.csv'
INTO TABLE demonstracoes_contabeis
FIELDS TERMINATED BY ';' ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@_data, @reg_ans, @cd_conta_contabil, @descricao, @vl_saldo_inicial, @vl_saldo_final) 
SET
    _data = STR_TO_DATE(@_data, '%Y-%m-%d'),
    reg_ans = CAST(@reg_ans AS UNSIGNED),
    cd_conta_contabil = CAST(@cd_conta_contabil AS UNSIGNED),
    descricao = TRIM(@descricao),
    vl_saldo_inicial = CAST(REPLACE(REGEXP_REPLACE(@vl_saldo_inicial, '[^0-9,.-]', ''), ',', '.') AS DECIMAL(10,2)),
    vl_saldo_final = CAST(REPLACE(REGEXP_REPLACE(@vl_saldo_final, '[^0-9,.-]', ''), ',', '.') AS DECIMAL(10,2));

LOAD DATA INFILE 'files/3T2024.csv'
INTO TABLE demonstracoes_contabeis
FIELDS TERMINATED BY ';' ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@_data, @reg_ans, @cd_conta_contabil, @descricao, @vl_saldo_inicial, @vl_saldo_final) 
SET
    _data = STR_TO_DATE(@_data, '%Y-%m-%d'),
    reg_ans = CAST(@reg_ans AS UNSIGNED),
    cd_conta_contabil = CAST(@cd_conta_contabil AS UNSIGNED),
    descricao = TRIM(@descricao),
    vl_saldo_inicial = CAST(REPLACE(REGEXP_REPLACE(@vl_saldo_inicial, '[^0-9,.-]', ''), ',', '.') AS DECIMAL(10,2)),
    vl_saldo_final = CAST(REPLACE(REGEXP_REPLACE(@vl_saldo_final, '[^0-9,.-]', ''), ',', '.') AS DECIMAL(10,2));

LOAD DATA INFILE 'files/4T2024.csv'
INTO TABLE demonstracoes_contabeis
FIELDS TERMINATED BY ';' ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@_data, @reg_ans, @cd_conta_contabil, @descricao, @vl_saldo_inicial, @vl_saldo_final) 
SET
    _data = STR_TO_DATE(@_data, '%Y-%m-%d'),
    reg_ans = CAST(@reg_ans AS UNSIGNED),
    cd_conta_contabil = CAST(@cd_conta_contabil AS UNSIGNED),
    descricao = TRIM(@descricao),
    vl_saldo_inicial = CAST(REPLACE(REGEXP_REPLACE(@vl_saldo_inicial, '[^0-9,.-]', ''), ',', '.') AS DECIMAL(10,2)),
    vl_saldo_final = CAST(REPLACE(REGEXP_REPLACE(@vl_saldo_final, '[^0-9,.-]', ''), ',', '.') AS DECIMAL(10,2));

 