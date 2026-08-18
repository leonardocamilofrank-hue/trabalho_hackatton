CREATE DATABASE IF NOT EXISTS reciclagem;

USE reciclagem;

CREATE TABLE IF NOT EXISTS materiais(
	id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    categoria VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS pontos_coleta(
	id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    endereco VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS coletas(
	id INT auto_increment PRIMARY KEY,
    material_id INT NOT NULL,
    ponto_id INT NOT NULL,
    quantidade DECIMAL(10,2) NOT NULL,
    data_coleta DATE NOT NULL,
    FOREIGN KEY (material_id) REFERENCES materiais(id), 
    FOREIGN KEY (ponto_id) REFERENCES pontos_coleta(id)
);