 import random
import os
import bisect
import time

# Funções para gerar dados aleatórios
def gerar_dados(num_registros):
    """Gera uma lista de strings, cada uma representando um registro com chave, dado1 e dado2."""
    dados = []
    for i in range(num_registros):
        chave = random.randint(1, num_registros)  # Chave inteira entre 1 e 10000
        dado1 = random.randint(0, 1000)   # dado1 inteiro entre 0 e 1000
        dado2 = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for i in range(1000))  # dado2 string de 1000 chars
        dados.append(f"{chave},{dado1},{dado2}\n")
    return dados

def salvar_dados_em_arquivo(nome_arquivo, dados):
    """Salva os dados em um arquivo de texto."""
    with open(nome_arquivo, 'w') as arquivo:
        arquivo.writelines(dados)

# Estrutura de dados sequencial (lista em Python)
class NoListaSequencial:
    def __init__(self, chave, dado1, dado2):
        self.chave = chave
        self.dado1 = dado1
        self.dado2 = dado2

class Sequencial:
    def __init__(self, nome_arquivo=None):  # Adiciona nome_arquivo como argumento opcional
        self.lista = []
        if nome_arquivo:  # Se nome_arquivo for fornecido
            self.carregar_dados(nome_arquivo)  # Carrega os dados do arquivo

    def carregar_dados(self, nome_arquivo):
        """Carrega os dados do arquivo para a lista."""
        with open(nome_arquivo, 'r') as arquivo:
            for linha in arquivo:
                chave, dado1, dado2 = linha.strip().split(',')
                self.inserir(int(chave), int(dado1), dado2) # Insere na lista

    def inserir(self, chave, dado1, dado2):
        no = NoListaSequencial(chave, dado1, dado2)
        self.lista.append(no)

    def buscar(self, _, chave):
        comparacoes = 0
        for no in self.lista:
            comparacoes += 1
            if no.chave == chave:
                return no, comparacoes
        return None, comparacoes

# Árvore binária não Balanceada
class No:
    def __init__(self, chave, dado1, dado2):
        self.chave = chave
        self.dado1 = dado1
        self.dado2 = dado2
        self.esquerda = None
        self.direita = None

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def inserir(self, chave, dado1, dado2):
        """Insere um novo nó na árvore binária."""
        novo_no = No(chave, dado1, dado2)
        if self.raiz is None:
            self.raiz = novo_no
        else:
            self._inserir_recursivo(self.raiz, novo_no)

    def _inserir_recursivo(self, no_atual, novo_no):
        """Insere recursivamente um nó na árvore."""
        if novo_no.chave < no_atual.chave:
            if no_atual.esquerda is None:
                no_atual.esquerda = novo_no
            else:
                self._inserir_recursivo(no_atual.esquerda, novo_no)
        else:
            if no_atual.direita is None:
                no_atual.direita = novo_no
            else:
                self._inserir_recursivo(no_atual.direita, novo_no)

    def buscar(self, chave):
        """Busca um registro com a chave especificada na árvore binária."""
        return self._buscar_recursivo(self.raiz, chave)

    def _buscar_recursivo(self, no_atual, chave, comparacoes=0):
        """Busca recursivamente um nó na árvore."""
        if no_atual is None:
            return None, comparacoes
        comparacoes += 1
        if no_atual.chave == chave:
            return no_atual, comparacoes
        elif chave < no_atual.chave:
            # Obtém o resultado e atualiza as comparações da chamada recursiva
            result, comparacoes = self._buscar_recursivo(no_atual.esquerda, chave, comparacoes)
            return result, comparacoes  # Retorna o resultado e as comparações atualizadas
        else:
            # Obtém o resultado e atualiza as comparações da chamada recursiva
            result, comparacoes = self._buscar_recursivo(no_atual.direita, chave, comparacoes)
            return result, comparacoes  # Retorna o resultado e as comparações atualizadas

# Árvore binária Balanceada (usando bisect para inserção ordenada)
class NoAVL:
    def __init__(self, chave, dado1, dado2):
        self.chave = chave
        self.dado1 = dado1
        self.dado2 = dado2
        self.esquerda = None
        self.direita = None
        self.altura = 1

class ArvoreBalanceada:
    def __init__(self, arquivo=None):
        self.raiz = None
        self.chaves = []
        if arquivo:
            with open(arquivo, 'r') as f:
                for linha in f:
                    chave, dado1, dado2 = linha.strip().split(',')
                    self.inserir(int(chave), int(dado1), dado2)

    def inserir(self, chave, dado1, dado2):
        self.raiz = self._inserir(self.raiz, chave, dado1, dado2)


    def _inserir(self, raiz, chave, dado1, dado2):
        if not raiz:
            return NoAVL(chave, dado1, dado2)
        elif chave < raiz.chave:
            raiz.esquerda = self._inserir(raiz.esquerda, chave, dado1, dado2)
        else:
            raiz.direita = self._inserir(raiz.direita, chave, dado1, dado2)

        raiz.altura = 1 + max(self.getAltura(raiz.esquerda),
                              self.getAltura(raiz.direita))

        fator_balanceamento = self.getFatorBalanceamento(raiz)

        # Caso 1 - Rotação simples à direita
        if fator_balanceamento > 1 and chave < raiz.esquerda.chave:
            return self.rotacaoDireita(raiz)

        # Caso 2 - Rotação simples à esquerda
        if fator_balanceamento < -1 and chave > raiz.direita.chave:
            return self.rotacaoEsquerda(raiz)

        # Caso 3 - Rotação dupla à direita
        if fator_balanceamento > 1 and chave > raiz.esquerda.chave:
            raiz.esquerda = self.rotacaoEsquerda(raiz.esquerda)
            return self.rotacaoDireita(raiz)

        # Caso 4 - Rotação dupla à esquerda
        if fator_balanceamento < -1 and chave < raiz.direita.chave:
            raiz.direita = self.rotacaoDireita(raiz.direita)
            return self.rotacaoEsquerda(raiz)

        return raiz

    def rotacaoEsquerda(self, z):
        y = z.direita

        # Verifica se y existe antes de acessar seus atributos
        if y is not None:
            T2 = y.esquerda

            # Realiza a rotação
            y.esquerda = z
            z.direita = T2

            # Atualiza alturas
            z.altura = 1 + max(self.getAltura(z.esquerda),
                           self.getAltura(z.direita))
            y.altura = 1 + max(self.getAltura(y.esquerda),
                           self.getAltura(y.direita))

            # Retorna a nova raiz
            return y
        else:
            # Lidar com o caso em que y é None
            return z  # ou gerar uma exceção, ou ajustar sua lógica de acordo

    def rotacaoDireita(self, z):
        y = z.esquerda

        # Verifica se y existe antes de acessar seus atributos
        if y is not None:
            T3 = y.direita

            # Realiza a rotação
            y.direita = z
            z.esquerda = T3

            # Atualiza alturas
            z.altura = 1 + max(self.getAltura(z.esquerda),self.getAltura(z.direita))
            y.altura = 1 + max(self.getAltura(y.esquerda),self.getAltura(y.direita))

           # Retorna a nova raiz
            return y
        else:
            # Lidar com o caso em que y é None
            return z  # ou gerar uma exceção, ou ajustar sua lógica de acordo

    def getAltura(self, raiz):
        if not raiz:
            return 0
        return raiz.altura

    def getFatorBalanceamento(self, raiz):
        if not raiz:
            return 0
        return self.getAltura(raiz.esquerda) - self.getAltura(raiz.direita)

    def buscar(self, chave):
        """Busca um registro com a chave especificada na árvore Balanceada."""
        return self._buscar_recursivo(self.raiz, chave)

    def _buscar_recursivo(self, no_atual, chave, comparacoes=0):
        """Busca recursivamente um nó na árvore."""
        if no_atual is None:
            return None, comparacoes

        comparacoes += 1  # Incrementa comparacoes antes da comparação da chave

        if chave == no_atual.chave:
            return no_atual, comparacoes  # Encontrou a chave
        elif chave < no_atual.chave:
            return self._buscar_recursivo(no_atual.esquerda, chave, comparacoes)
        else:
            return self._buscar_recursivo(no_atual.direita, chave, comparacoes)


# Função para medir o tempo de execução e comparações
def analisar_desempenho(estrutura, chave_busca):
    """Analisa o desempenho da busca em uma estrutura de dados."""
    inicio = time.time()

    # Verifica o tipo da estrutura para chamar o método buscar correto
    if isinstance(estrutura, Sequencial):
        result = estrutura.buscar(None, chave_busca)  # Para Sequencial, mantém os dois argumentos
    else:
        result = estrutura.buscar(chave_busca)  # Para outras estruturas, usa apenas a chave

    # Verifica se a chave foi encontrada e extrai os resultados
    if result is not None:
        registro, comparacoes = result
    else:  # Se a chave não foi encontrada
        registro, comparacoes = result

    fim = time.time()
    tempo_execucao = fim - inicio

    return tempo_execucao, comparacoes

def executar_experimentos(tamanhos_arquivos):
    """Executa experimentos de busca para diferentes tamanhos de arquivo."""
    resultados = []
    for tamanho in tamanhos_arquivos:
        nome_arquivo = f"dados_{tamanho}.txt"
        dados = gerar_dados(tamanho)
        salvar_dados_em_arquivo(nome_arquivo, dados)

        sequencial = Sequencial(nome_arquivo)

        # Criar árvore binária não Balanceada e inserir dados
        arvore_binaria = ArvoreBinaria()
        with open(nome_arquivo, 'r') as f:
            for linha in f:
                chave, dado1, dado2 = linha.strip().split(',')
                arvore_binaria.inserir(int(chave), int(dado1), dado2)

        arvore_Balanceada = ArvoreBalanceada(nome_arquivo)

        chave_busca = random.randint(1, 10000)  # Busca por uma chave aleatória

        # Analisando a busca sequencial
        tempo_sequencial, comparacoes_sequencial = analisar_desempenho(sequencial, chave_busca)

        # Analisando a busca em árvore binária não Balanceada
        tempo_arvore_binaria, comparacoes_arvore_binaria = analisar_desempenho(arvore_binaria, chave_busca)

        # Analisando a busca em árvore Balanceada
        tempo_arvore, comparacoes_arvore = analisar_desempenho(arvore_Balanceada, chave_busca)

        resultados.append({
            'tamanho': tamanho,
            'tempo_sequencial': tempo_sequencial,
            'comparacoes_sequencial': comparacoes_sequencial,
            'tempo_arvore_binaria': tempo_arvore_binaria,
            'comparacoes_arvore_binaria': comparacoes_arvore_binaria, # Fixed the typo here (removed extra space)
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

# Tamanhos dos arquivos a serem testados
tamanhos_arquivos = [100, 500, 1000, 5000, 10000]

nome_arquivo = 'dados_ordenados.txt'
print(f"Dados gerados e salvos em '{nome_arquivo}'")
# Gerar e salvar dados ordenados
for tamanho in range(5):

    num_registros = tamanhos_arquivos[tamanho]
    dados = gerar_dados(num_registros)
    salvar_dados_em_arquivo(nome_arquivo, dados)

nome_arquivo = 'dados_nao_ordenados.txt'
print(f"Dados gerados e salvos em '{nome_arquivo}'")
for tamanho in range(5):
    # Gerar e salvar dados não ordenados
    num_registros = tamanhos_arquivos[tamanho]
    dados = gerar_dados(num_registros)
    random.shuffle(dados)  # Embaralha os dados para gerar chaves não ordenadas
    salvar_dados_em_arquivo(nome_arquivo, dados)

# Executar experimentos
resultados = executar_experimentos(tamanhos_arquivos)

# Imprimir os resultados dos experimentos
for resultado in resultados:
    print(f"Tamanho do arquivo: {resultado['tamanho']}")
    print(f"  Tempo Sequencial: {resultado['tempo_sequencial']:.6f} segundos, Comparações: {resultado['comparacoes_sequencial']}")
    print(f"  Tempo Arvore Binária: {resultado['tempo_arvore_binaria']:.6f} segundos, Comparações: {resultado['comparacoes_arvore_binaria']}")
    print(f"  Tempo Arvore Balanceada: {resultado['tempo_arvore']:.6f} segundos, Comparações: {resultado['comparacoes_arvore']}")
    print("-" * 20)

# Exemplo de uso com os arquivos 'dados_ordenados.txt' e 'dados_nao_ordenados.txt'
arquivos = ['dados_ordenados.txt', 'dados_nao_ordenados.txt']

for arquivo in arquivos:
    sequencial = Sequencial(arquivo)

    # Criar árvore binária não Balanceada e inserir dados
    arvore_binaria = ArvoreBinaria()
    with open(arquivo, 'r') as f:
        for linha in f:
            chave, dado1, dado2 = linha.strip().split(',')
            arvore_binaria.inserir(int(chave), int(dado1), dado2)

    arvore_Balanceada = ArvoreBalanceada(arquivo)

    chaves_existentes = [no.chave for no in sequencial.lista]

    chaves_presentes = random.sample(chaves_existentes, 15)

    # Gerando chaves inexistentes
    chaves_ausentes = []
    while len(chaves_ausentes) < 15:
        chave = random.randint(1, 20000)
        if chave not in chaves_existentes and chave not in chaves_ausentes:
            chaves_ausentes.append(chave)

    resultados_sequencial = buscar_chaves(sequencial, chaves_presentes, chaves_ausentes)
    resultados_arvore_binaria = buscar_chaves(arvore_binaria, chaves_presentes, chaves_ausentes)
    resultados_arvore = buscar_chaves(arvore_Balanceada, chaves_presentes, chaves_ausentes)

    print(f"Resultados para o arquivo: {arquivo}")
    print("Sequencial:")
    for resultado in resultados_sequencial:
        print(resultado)

    print("\nArvore Binária:")
    for resultado in resultados_arvore_binaria:
        print(resultado)

    print("\nArvore Balanceada:")
    for resultado in resultados_arvore:
        print(resultado)

    print("-" * 40)
