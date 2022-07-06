
BEGIN TRANSACTION;

CREATE TABLE pessoas (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    CPF      TEXT        NOT NULL,
    NOME     TEXT        NOT NULL,
    IDADE    INT         NOT NULL,
    ENDERECO    CHAR(50),
    SALARIO     REAL   
);
COMMIT;

BEGIN TRANSACTION;

INSERT INTO (CPF, NOME, IDADE, ENDERECO, SALARIO)
VALUES('111.318.679-80', 'Victor Hugo', 24, 'Rua das flores', 1300,00)   
);
COMMIT;