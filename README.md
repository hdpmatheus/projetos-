# Estrutura de Dados e Análise de Desempenho com Python

Este projeto contém um conjunto de funções e classes Python para gerar dados aleatórios, armazená-los em arquivos e comparar o desempenho de buscas utilizando uma estrutura de dados sequencial (lista) e uma árvore binária balanceada.

## Funcionalidades

O código realiza as seguintes operações principais:

1. **Geração de Dados Aleatórios**: Gera registros com chaves numéricas, valores inteiros e strings de caracteres aleatórios.
2. **Armazenamento em Arquivo**: Salva os dados gerados em arquivos de texto para posterior análise.
3. **Estruturas de Dados para Busca**:
   - **Sequencial**: Utiliza uma lista para armazenar os dados de forma sequencial e realizar buscas iterativas.
   - **Árvore Binária Balanceada**: Implementa uma árvore usando a biblioteca `bisect` para inserções ordenadas e busca binária.
4. **Análise de Desempenho**: Mede o tempo de execução e o número de comparações para cada busca em ambas as estruturas.

## Instalação

Para executar o projeto, é necessário possuir o Python (3.6 ou superior)

1. **Clone o Repositório**:
   ```bash
   git clone https://github.com/hdpmatheus/main.git
   cd main
   ´´´
 Execute o script principal:
    ```bash
        python trabalhoaeds.py
    ```
  A saída esperada será: 

  Dados gerados e salvos em 'dados_ordenados.txt'
 
  Dados gerados e salvos em 'dados_nao_ordenados.txt'
  
  Resultados para o arquivo: dados_ordenados.txt
  
  Sequencial:
  
  ...
  
  Arvore:
  
  ...


  ## Exemplo de uso


# Geração de dados

num_registros = 1000
dados = gerar_dados(num_registros)
salvar_dados_em_arquivo('dados_exemplo.txt', dados)


# Inicialização das Estruturas de Dados

sequencial = Sequencial('dados_exemplo.txt')
arvore_balanceada = ArvoreBalanceada('dados_exemplo.txt')


# Execução de Experimentos de Desempenho

tamanhos_arquivos = [100, 500, 1000, 5000]
resultados = executar_experimentos(tamanhos_arquivos)
for resultado in resultados:
    print(resultado)



