**Aula dia 14/07/2022**
- Usos apropriados para o SQLITE
    -  Cliente/Servidor: É uma aplicação que esta instalada em um computador e ligada diretamente a um serivdor, alguams dessas aplicações são, MySQL, Oracle, PostgreSQL
    - O SQLITE serve para armazenar dados localmente e pode se dizer q o SQLITE não é um concorrente dos outros bancos que são cliente/servidor
- Algumas situações para se usar o SQLITE
    - Dispositivos incorporados(Embedded devices), o sql é muito usado por permitir um formato de arquivo de aplicativo, ou seja, não é necessario baixar muitos arquivos para trabalhar com a base de dados, sites com baixo trafego ou seja com poucos acessos e poucas inflações de dados e é muito usado tambem para analise de dados
    - Cliente/servidor é preferivel usar em datacenters
- SQLITE usado na analise de dados
    - Para analises é muito mais simples usar sqlite, pois devida a sua facilidade de instalação e por ser muito leve, acaba sendo algo mais agil do que outros bancos, então analises basicas podem ser feitas de maneiras muito rapidas e agilizando muito o processo
- SQLITE em dados corporativos
- Banco de dados ao lado do servidor
    - Para reduzir processamentos em SGBD usasse arquivos sqlite para tercerizar esses acessos dados de uma base principal
- Tranferencia de dados
    - Quando se pretende tranferir uma grande quantidade de dados, atraves de comandos sql ele cria arquivos zip para tranferir os dados para outros servidores servindo como um container
- Bancos de dados internos ou temporarios
    - Demos ou testes
    - Educação e Treinamento
    - Extensões de SQL Experimental
        - Tudo oq ue pode ser usado como prototipo para usar como testes ou temporariamente é muito facil usar o sqlite 
- QUando não usar o SQLite e usar um (RDBMS) sistema de gerenciamento de banco de dados relacional
    - Aplicativos Client/Server
    - Sites de alto volume
    - Conjuntos de dados muito grandes
    - Alta simultaneidade(O SQLite permite inumeras leituras mas não permite escritas simultaneas por duas ou mais conexões)
- Listas de verificação para escolher o melhor mecanismo de banco de dados
    - Escolha cliente/servidor quando: os dados são separados do aplicativo por uma rede
    - Muitos escritores simultaneos
    - Dados de tipo muito grandes
- Caso Contrario use o SQLite

**Aula dia 15/07/2022**
- VSCODE C/SQLite
- criar dump
    - .output dump.sql
    - .dump
    
