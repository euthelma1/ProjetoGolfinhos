import networkx as nx


# Função para ler o arquivo e criar o grafo
def ler_grafo(arquivo):
    grafo = nx.Graph()  # Cria um grafo vazio não direcionado
    with open(arquivo, 'r') as f:  # Abre o arquivo de entrada em modo de leitura
        for linha in f:
            linha = linha.strip()  # Remove espaços extras no início e no fim da linha
            if linha.startswith('%') or not linha:  # Ignora linhas que começam com % (comentários) ou estão vazias
                continue  # Ignora comentários e linhas vazias
            valores = linha.split()  # Divide a linha em uma lista de strings.
            if len(valores) == 2:  # Verifica se há apenas dois valores na linha para evitar de ler a primeira linha 62 62 159
                u, v = map(int, valores)  # Converte esses valores em inteiros 
                grafo.add_edge(u, v)  # Adiciona uma aresta entre os vértices u e v no grafo
    return grafo

# Função para calcular e imprimir o grau dos vértices
def grau_dos_vertices(grafo):
    print("\nGraus dos Vértices:")
    for vertice, grau in grafo.degree():  # Retorna uma lista de tuplas, onde cada tupla contém um vértice e seu grau.
        print(f"Vértice {vertice}: Grau {grau}")
        
        
        
# Função para calcular e imprimir o coeficiente de aglomeração de cada vértice
def coeficiente_aglomeracao(grafo):
    def calcular_aglomeracao(grafo, vertice):
        vizinhos = list(grafo.neighbors(vertice))  # Lista de vizinhos do vértice
        num_vizinhos = len(vizinhos)
        
        if num_vizinhos < 2:  # Um vértice com menos de dois vizinhos tem coeficiente de aglomeração 0
            return 0.0
        
        # Conta o número de conexões entre os vizinhos
        conexoes_entre_vizinhos = 0
        for i in range(num_vizinhos):
            for j in range(i + 1, num_vizinhos):
                if grafo.has_edge(vizinhos[i], vizinhos[j]):  # Se os vizinhos estão conectados
                    conexoes_entre_vizinhos += 1
        
        # Total de pares possíveis de vizinhos
        total_pares_possiveis = num_vizinhos * (num_vizinhos - 1) / 2
        
        # Coeficiente de aglomeração para o vértice
        return conexoes_entre_vizinhos / total_pares_possiveis

    # Calcula o coeficiente de aglomeração para cada vértice
    coeficientes = {}
    for vertice in grafo.nodes:
        coeficientes[vertice] = calcular_aglomeracao(grafo, vertice)

    # Imprime os coeficientes de cada vértice
    print("\nCoeficiente de Aglomeração de Cada Vértice:")
    for vertice, coef in coeficientes.items():
        print(f"Vértice {vertice}: Coeficiente de Aglomeração {coef:.2f}")

    # Calcula o coeficiente médio de aglomeração
    coef_medio = sum(coeficientes.values()) / len(coeficientes)
    print(f"\nCoeficiente Médio de Aglomeração do Grafo: {coef_medio}")

