CREATE DATABASE PessoaDB;

USE PessoaDB;

CREATE TABLE Pessoas (
    id INT PRIMARY KEY IDENTITY(1,1),
    apelido VARCHAR(32) NOT NULL UNIQUE,
    nome VARCHAR(100) NOT NULL,
    nascimento DATE NOT NULL
);
