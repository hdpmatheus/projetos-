import random
import os
import bisect
import time

# Funções para gerar dados aleatórios
def gerar_dados(num_registros):
  """Gera uma lista de strings, cada uma representando um registro com chave, dado1 e dado2."""
  dados = []
  for _ in range(num_registros):
    chave = random.randint(1, 10000)  # Chave inteira entre 1 e 10000
    dado1 = random.randint(0, 1000)   # dado1 inteiro entre 0 e 1000
    dado2 = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for i in range(1000)) # dado2 string de 1000 chars
    dados.append(f"{chave},{dado1},{dado2}\n")
  return dados

def salvar_dados_em_arquivo(nome_arquivo, dados):
    """Salva os dados em um arquivo de texto."""
    with open(nome_arquivo, 'w') as arquivo:
        arquivo.writelines(dados)

# Estrutura de dados sequencial (lista em Python)
class Sequencial:
    def __init__(self, arquivo):
        """Inicializa a estrutura de dados sequencial lendo dados de um arquivo."""
        self.dados = []
        with open(arquivo, 'r') as f:
            for linha in f:
                chave, dado1, dado2 = linha.strip().split(',')
                self.dados.append({'chave': int(chave), 'dado1': int(dado1), 'dado2': dado2})

    def buscar(self, chave):
        """Busca um registro com a chave especificada."""
        for registro in self.dados:
            if registro['chave'] == chave:
                return registro
        return None

# Árvore binária balanceada (usando bisect para inserção ordenada)
class ArvoreBalanceada:
    def __init__(self, arquivo):
        """Inicializa a árvore balanceada lendo dados de um arquivo."""
        self.chaves = []
        self.dados = []
        with open(arquivo, 'r') as f:
            for linha in f:
              chave, dado1, dado2 = linha.strip().split(',')
              bisect.insort(self.chaves, int(chave)) # Insere e mantém ordenado
              self.dados.append({'chave':int(chave), 'dado1':int(dado1), 'dado2':dado2})

    def buscar(self, chave):
      """Busca um registro com a chave especificada na árvore balanceada."""
      i = bisect.bisect_left(self.chaves, chave)
      if i != len(self.chaves) and self.chaves[i] == chave:
        return self.dados[i]
      return None

# Função para medir o tempo de execução e comparações
def analisar_desempenho(estrutura, chave_busca):
    """Analisa o desempenho da busca em uma estrutura de dados."""
    inicio = time.time()
    comparacoes = 0
    registro = estrutura.buscar(chave_busca)
    fim = time.time()
    tempo_execucao = fim - inicio
    
    if isinstance(estrutura, Sequencial):
      comparacoes = len(estrutura.dados) if registro is None else estrutura.dados.index(registro) +1
    elif isinstance(estrutura, ArvoreBalanceada):
      i = bisect.bisect_left(estrutura.chaves, chave_busca)
      comparacoes = i+1
    return tempo_execucao, comparacoes

def executar_experimentos(tamanhos_arquivos):
    """Executa experimentos de busca para diferentes tamanhos de arquivo."""
    resultados = []
    for tamanho in tamanhos_arquivos:
        nome_arquivo = f"dados_{tamanho}.txt"
        dados = gerar_dados(tamanho)
        salvar_dados_em_arquivo(nome_arquivo, dados)

        sequencial = Sequencial(nome_arquivo)
        arvore_balanceada = ArvoreBalanceada(nome_arquivo)

        chave_busca = random.randint(1, 10000)  # Busca por uma chave aleatória

        # Analisando a busca sequencial
        tempo_sequencial, comparacoes_sequencial = analisar_desempenho(sequencial, chave_busca)

        # Analisando a busca em árvore balanceada
        tempo_arvore, comparacoes_arvore = analisar_desempenho(arvore_balanceada, chave_busca)

        resultados.append({
            'tamanho': tamanho,
            'tempo_sequencial': tempo_sequencial,
            'comparacoes_sequencial': comparacoes_sequencial,
            'tempo_arvore': tempo_arvore,
            'comparacoes_arvore': comparacoes_arvore
        })
    return resultados

def buscar_chaves(estrutura, chaves_presentes, chaves_ausentes):
    """Busca um conjunto de chaves em uma estrutura de dados, incluindo chaves presentes e ausentes."""
    resultados = []
    for chave in chaves_presentes:
        tempo, comparacoes = analisar_desempenho(estrutura, chave)
        resultados.append({'chave': chave, 'presente': True, 'tempo': tempo, 'comparacoes': comparacoes})
    for chave in chaves_ausentes:
        tempo, comparacoes = analisar_desempenho(estrutura, chave)
        resultados.append({'chave': chave, 'presente': False, 'tempo': tempo, 'comparacoes': comparacoes})
    return resultados

# Gerar e salvar dados ordenados
num_registros = 1000
dados = gerar_dados(num_registros)
nome_arquivo = 'dados_ordenados.txt'
salvar_dados_em_arquivo(nome_arquivo, dados)
print(f"Dados gerados e salvos em '{nome_arquivo}'")

# Gerar e salvar dados não ordenados
num_registros = 1000
dados = gerar_dados(num_registros)
random.shuffle(dados)  # Embaralha os dados para gerar chaves não ordenadas
nome_arquivo = 'dados_nao_ordenados.txt'
salvar_dados_em_arquivo(nome_arquivo, dados)
print(f"Dados gerados e salvos em '{nome_arquivo}'")

# Tamanhos dos arquivos a serem testados
tamanhos_arquivos = [100, 500, 1000, 5000, 10000]

# Executar experimentos
resultados = executar_experimentos(tamanhos_arquivos)

# Imprimir os resultados dos experimentos
for resultado in resultados:
    print(f"Tamanho do arquivo: {resultado['tamanho']}")
    print(f"  Tempo Sequencial: {resultado['tempo_sequencial']:.6f} segundos, Comparações: {resultado['comparacoes_sequencial']}")
    print(f"  Tempo Arvore: {resultado['tempo_arvore']:.6f} segundos, Comparações: {resultado['comparacoes_arvore']}")
    print("-" * 20)


# Exemplo de uso com os arquivos 'dados_ordenados.txt' e 'dados_nao_ordenados.txt'
arquivos = ['dados_ordenados.txt', 'dados_nao_ordenados.txt']

for arquivo in arquivos:
    sequencial = Sequencial(arquivo)
    arvore_balanceada = ArvoreBalanceada(arquivo)
    
    chaves_existentes = [registro['chave'] for registro in sequencial.dados]
    chaves_presentes = random.sample(chaves_existentes, 15)
    
    # Gerando chaves inexistentes
    chaves_ausentes = []
    while len(chaves_ausentes) < 15:
        chave = random.randint(1, 20000)
        if chave not in chaves_existentes and chave not in chaves_ausentes:
            chaves_ausentes.append(chave)
            
    resultados_sequencial = buscar_chaves(sequencial, chaves_presentes, chaves_ausentes)
    resultados_arvore = buscar_chaves(arvore_balanceada, chaves_presentes, chaves_ausentes)
    
    print(f"Resultados para o arquivo: {arquivo}")
    print("Sequencial:")
    for resultado in resultados_sequencial:
        print(resultado)
    
    print("\nArvore:")
    for resultado in resultados_arvore:
        print(resultado)
    print("-" * 40)
