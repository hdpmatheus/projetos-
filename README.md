# Estrutura de Dados e Análise de Desempenho com Python

Este projeto contém um conjunto de funções e classes Python para gerar dados aleatórios, armazená-los em arquivos e comparar o desempenho de buscas utilizando diferentes estruturas de dados: Lista Sequencial, Árvore Binária não Balanceada e Árvore Binária Balanceada (AVL). O objetivo é avaliar e comparar o tempo de execução e o número de comparações de cada estrutura ao realizar operações de busca.

## Índice
- [Funcionalidades](#funcionalidades)
- [Estruturas de Dados Implementadas](#estruturas-de-dados-implementadas)
- [Instalação](#instalação)
- [Execução](#execução)
- [Exemplo de Uso](#exemplo-de-uso)
- [Resultados Esperados](#resultados-esperados)


## Funcionalidades

Este projeto realiza as seguintes operações principais:

1. **Geração de Dados Aleatórios**: Gera registros com chaves numéricas, valores inteiros e strings aleatórias.
2. **Armazenamento em Arquivo**: Salva os dados gerados em arquivos de texto para posterior análise.
3. **Estruturas de Dados para Busca**:
   - **Lista Sequencial**: Utiliza uma lista para armazenar os dados de forma sequencial e realizar buscas iterativas.
   - **Árvore Binária não Balanceada**: Implementa uma árvore binária onde cada nó pode ter uma subárvore esquerda e direita.
   - **Árvore Binária Balanceada (AVL)**: Implementa uma árvore balanceada que utiliza rotações para manter o equilíbrio e minimizar o tempo de busca.
4. **Análise de Desempenho**: Mede o tempo de execução e o número de comparações realizadas em cada busca para cada estrutura de dados.

## Estruturas de Dados Implementadas

### 1. Lista Sequencial
Armazena registros linearmente em uma lista. A busca é realizada de forma sequencial, resultando em uma complexidade de O(n) no pior caso.

### 2. Árvore Binária não Balanceada
Armazena dados de forma hierárquica, dividindo-os entre uma subárvore esquerda e direita. Embora tenha complexidade média de O(log n), pode degradar para O(n) em caso de desbalanceamento.

### 3. Árvore Binária Balanceada (AVL)
Uma árvore AVL mantém o equilíbrio através de rotações (simples e duplas), assegurando uma complexidade de busca de O(log n) em todos os casos, o que torna o processo de busca mais eficiente em grandes volumes de dados.

## Instalação

Para executar o projeto, é necessário ter o Python (3.6 ou superior) instalado.

1. **Clone o Repositório**:
   ```bash
   git clone https://github.com/hdpmatheus/main.git
   cd main


## Execução 

Execute o script principal

python trabalhoaeds.py

A saída esperada será similar à: 

Dados gerados e salvos em 'dados_ordenados.txt'
Dados gerados e salvos em 'dados_nao_ordenados.txt'

Resultados para o arquivo: dados_ordenados.txt

Sequencial:
...

Arvore Binária:
...

Arvore AVL:
...

## Exemplo de Uso

### Geração de dados 
num_registros = 1000
dados = gerar_dados(num_registros)
salvar_dados_em_arquivo('dados_exemplo.txt', dados)

### Inicialização das Estruturas de Dados 
sequencial = Sequencial('dados_exemplo.txt')
arvore_binaria = ArvoreBinaria()
arvore_balanceada = ArvoreBalanceada('dados_exemplo.txt')

### Execução de Experimentos de Desempenho
tamanhos_arquivos = [100, 500, 1000, 5000]
resultados = executar_experimentos(tamanhos_arquivos)
for resultado in resultados:
    print(resultado)

## Resultados Esperados 
A análise de desempenho compara o tempo de execução e o número de comparações realizadas em cada tipo de estrutura de dados para diferentes tamanhos de entrada. Espera-se que a Árvore AVL apresente o menor tempo de busca e menor número de comparações devido ao balanceamento, seguida pela Árvore Binária e, por último, pela Lista Sequencial, que apresenta um crescimento linear no número de comparações conforme o aumento dos dados.
