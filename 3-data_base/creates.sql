CREATE DATABASE intuitive_care;

USE intuitive_care;

CREATE TABLE operadoras_de_plano_de_saude_ativas (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    registro_ans INT UNSIGNED NOT NULL UNIQUE,
    cnpj VARCHAR(14) NOT NULL UNIQUE,
    razao_social VARCHAR(255) NOT NULL,
    nome_fantasia VARCHAR(255),
    modalidade VARCHAR(255) NOT NULL,
    logradouro VARCHAR(255) NOT NULL,
    numero VARCHAR(12) NOT NULL,
    complemento VARCHAR(255),
    bairro VARCHAR(255) NOT NULL,
    cidade VARCHAR(255) NOT NULL,
    uf VARCHAR(2) NOT NULL,
    cep VARCHAR(8) NOT NULL,
    ddd VARCHAR(3) NOT NULL,
    telefone VARCHAR(10) NOT NULL,
    fax VARCHAR(10),
    endereco_eletronico VARCHAR(255) NOT NULL,
    representante VARCHAR(255) NOT NULL,
    cargo_representante VARCHAR(255) NOT NULL,
    regiao_de_comercializacao VARCHAR(255) NOT NULL,
    data_registro_ans DATE NOT NULL
);

CREATE TABLE demonstracoes_contabeis (
	id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    _data DATE NOT NULL,
    reg_ans INT UNSIGNED NOT NULL,
    cd_conta_contabil INT NOT NULL,
    descricao VARCHAR(255),
    vl_saldo_inicial DECIMAL(10,2) NOT NULL,
    vl_saldo_final DECIMAL(10,2) NOT NULL,

    CONSTRAINT ct_demonstracoes_contabeis_reg_ans FOREIGN KEY (reg_ans) 
    REFERENCES operadoras_de_plano_de_saude_ativas (registro_ans) 
    ON DELETE CASCADE ON UPDATE CASCADE
);