CREATE TABLE cliente (
    id INT PRIMARY KEY AUTO_INCREMENT, 
    nome VARCHAR(100) NOT NULL,
    email VARCHAR (100) NOT NULL UNIQUE,
    telefone VARCHAR(20),
    data_nascimento DATE,
    saldo DECIMAL(10,2),
    ativo BOOLEAN DEFAULT TRUE,
    cadastrado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    
    CREATE TABLE cliente(
    id INT AUTO_INCREMENT PRIMARY KEY,
    telefone VARCHAR(20) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    data_nascimento DATE NOT NULL,
    senha VARCHAR(2550)
    );
    