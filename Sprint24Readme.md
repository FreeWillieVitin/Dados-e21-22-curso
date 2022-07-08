**Aula dia 24/06/2022**
- Introdução ao banco de dados(Até que enfim <3)
    - O que é SQL: Structured query language(Linguagem de consulta estruturada)
    - Query: Consultas (Inclusão, alteraçao e exclusão) 
    - Triggers <3(Gatilhos que disparam ações apos realizar alguma query)
    - Views: (Visualizador automatizados, são querys pré- programados)
    - SGBD: Sistema gerenciador de banco de dados(MySql, SQL Server, Oracle server e muitos outros)
    - SQLite: Server para desenvolver aplicações python
    - DashBoard: Um visualizador de graficos normal com funções e botoes
- Diferença entra DBA e analista de dados
    - Analista transforma ao dado em informações uteis e trabalhaveis, DBA é um admnistrador do banco que gerencia e trabalha com a manutenção, 
    aprimoramento e etc

**Aula dia 28/06/2022**
- o que é um banco de dados:
    - Conjunto de informações organizadas em um formato onde os dados são:
        - Armazenados
        - Gerenciados
        - Atualizados
        - Recuperados
    - Existem 2 tipos de bancos de dados:
        - Banco de dados Relacionais
            - Bancos de dados relacioanis é caracterizado pela forma como os dados são organizados
            - Tabelas respeitam um SCHEMA. Determina como as tabelas devem ser compostas
            (Linhas e Colunas)
        - Banco de dados Não relacionais(NoSQL)
    - Tabelas ou entidades
    - Colunas ou tributo: unidade que armazena um tipo de valor
    - Linhas ou tupla: São todos os dados referentes a um item
- Tipos de dados existentes nas colunas:
    - text: Tipo de texto
    - integer: Tipos numéricos inteiros
    - real: Tipos numericos reias
    - null: Valor Nulo
    - blob: Verdadeiro ou falso
- Chaves (Primaria e estrangeira)
    - Chave primaria: Server para dar exclusividade para um registro na tabela ou seja valores que nao podem se repetir
        - Regras da chave primaria
            - O valor deve ser unico
            - Não pode nunca ser alterada
            - Não pode ser valor null
    - Chave Estrangeira(Foreign Key - FK): è o que referencia uma chave primaria em outra tabela
- Relacionamento entre tabelas / Entidades:
    - Relacioonamento é a associação entre as tabelas, que sao conectadas por chaves primarias(PK), Chaves Estrangeiras(FK)
    - Tipos de relacionamento:
        1:1 - Relacionamento em 1 linhas de uma tabelas com 1 linha de outra tabelas.
        1:N - Relacionamento de 1 linha de uma tabela com muitas linhas de outras tabelas.
        N:N - Relacionamentos de muitas linhas de uma tabela com muitas linhas de outra tabela

**Aula dia 30/06/2022**
- Auto Relacionamento: Relacionamento de uma linha de uma mesma tabela com outra linha da mesma tabela

- Modelo De Dados
    - São formas visuais de mostrar a organização de uma base
- Modelo de Dados Relacionais
    - São formas visuais que mostram como cada entidade se organiza

- Ferramentas de diagramas(diagrams.net, brmodelo, pode ser feito no paint, quickdatabasediagrams.com, dbeaver)

**Aula dia 05/07/2022**
- SQL
    - Linguagem de comunicação com o banco de dados
    - Sempre precisa de um cliente para conversar com um banco
    - Structured Query Language
- Organização
    - SQL é dividido em 5 modelos(DDL, DCL, DTL, DML, DQL)
    - DDL: Criação/Manutenção: Create, alter, drop
    - DCL: COntrole de dados: Grant, Revoke
    - DTL: GErenciamento de transações: Begin, Commit, Rollback
    - DML: MAnipulação de dados: Insert, update, delete
    - DQL: COnsulta: Select
- DDL(Data Definition Language)
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
        ALTER TABLE TESTE 
        ADD COLUMN ALTURA DECIMAL(10,2); 

        DROP TABLE TESTE;

- Mais atributos da table
    - Auto Increment: Insere registros automaticamente valores aos campos seguindo uma ordem

- Inserir dados em uma table
    BEGIN TRANSACTION;
        INSERT INTO TESTE(CPF, NOME, IDADE)
        VALUES (111.318.679-80, "VICTOR HUGO", 24)
    COMMIT;
- select
    select * from pessoas    

**Aula dia 07/07/2022**
- Select
    - Select é usado para selecionar dados
    - Distinct: Função que seleciona apenas registros que não são repetidos
    - Where: Define um parametro de busca onde
-  Operadores Logicos
    - IN, Like, And, Or, Between
    - IN: Retorna 1 se o valor testado estiver na lista
    - LIKE: Retorna 1 se o valor testado coincidir com o padrão passado
    - AND: Retorna 1 se as duas expressoes testadas forem 1
    - OR: Retorna 1 se uma das duas expressores testadas forem 1
    - BETWEEN: Retrona 1 se o valor testado estiver no intervalo passado
- Order By
    - Função sql que ordena os dados de uma tabela
    - Se for inserido desc, vai ordenar a tabela de forma decrescente
- Funções de agregação
    - AVG, MIN, MAX, SUM, COUNT¨
    - AVG: Faz o calculo da media, de uma coluna com dados inteiros
    - MIN: Retorna o menor valor
    - MAX: Retorna o maior valor
    - SUM: Retorna a soma de valores
    - COUNT: Conta a quantidade de linhas em uma tabela
    - Group By: Agrupa valores de u8ma tabela
- Junção de tabelas
    - Uso de joins serve para juntar dados de uma tabela com a outra




