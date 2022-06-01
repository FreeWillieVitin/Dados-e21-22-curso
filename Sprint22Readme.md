**Aula dia 30/05/2022**
- python -m venv venv se estiver na pasta ja(Cria um ambiente virtual)
- pip freeze > requirements.txt(criar os requirements)
- pip install -r requirements.txt(Instala o requirements) 

**Aula dia 31/05/2022**
- Devido problemas de conexão a ula se iniciou de forma diferente
- inicio a programação orientada a objeto(POO)
    - Objetos e classes
    - Objetos é um elemento que pode ser chamado de variavel e que tem tenha o seu espaço em memoria alocado e um conjunto de
    de operações associadas a ele "Em python tudo é um oobjeto"
    - uma classe é uma descrição que abstrai um conjunto de objetos com características similares
        - Nas boas praticas de programação o certo seria sempre iniciar o nome de uma classe com letra maiuscula na sua criação
    - Estruturas de dados que guardam em si uma infinidade de estruturas de dados
    - Variaveis x Objetos: 
    * Variavel é um espaço de memoria alocado onde guardamos um valor de forma estatica
    - Tudo o que for codificado em uma classe servirá de interação para outros objetos
    - Leitura lexica do interpretador significa o interpretador vai ler os codigos da seguinte ordem, sempre da esquerda para direita e linha apos linha
    - Método Contrutor de uma classe
        - Método é uma função interna que recebe parametros de classes(atributos da classe), ele pode ser chamado de inicializador
        - função __init__(self, ...) função reservada do sistema que indica a inicialização dentro de uma classe e roda a classe dentro da função quando é inicializada(Self é apenas uma referencia que indica que os dados serão guardados dentro da classe)
    - Identação