BEGIN TRANSACTION;

drop TABLE IF EXISTS cidades;

create table cidades (
    id_cidade INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_cidade varchar(50) NOT NULL
);

drop TABLE IF EXISTS pessoas;

CREATE TABLE pessoas (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    CPF      varchar(14) NOT NULL,
    NOME     varchar(50) NOT NULL,
    IDADE    INTEGER     NOT NULL,
    ENDERECO    VARCHAR(50),
    SALARIO     REAL,
    ID_CIDADE VARCHAR(30)   
);

INSERT INTO cidades (nome_cidade)
    VALUES ('Mafra'),
    ('Rio Negro'),
    ('Curitiba'),
    ('São Bento do Sul');

INSERT INTO pessoas (CPF, NOME, IDADE, ENDERECO, SALARIO, ID_CIDADE)
    VALUES ('111.318.679-80', 'Victor Hugo', 24, 'Rua das flores', 1300.00, 1),
    ('333.444.555-90', 'Marieli Stankievski', 23, 'Rua das flores', 1300.00, 4),
    ('111.318.679-80', 'Jorge', 68, 'Rua das flores', 1300.00, 3),    
    ('111.318.679-80', 'James', 25, 'Rua das flores', 1300.00, 2);

COMMIT;

SELECT * FROM cidades;
SELECT * FROM pessoas;