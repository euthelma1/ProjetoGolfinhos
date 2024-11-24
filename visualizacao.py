
import networkx as nx
import matplotlib.pyplot as plt
import networkx.algorithms.clique as clique
import random

# Função para visualizar o grafo com cliques maximais coloridos
def visualizar_grafo(grafo):
    # Gera posições para os nós
    pos = nx.spring_layout(grafo)

    # Encontra todos os cliques maximais no grafo
    cliques = list(clique.find_cliques(grafo))

    # Gera cores diferentes para cada clique
    num_cliques = len(cliques)
    cores = [f"#{''.join(random.choices('0123456789ABCDEF', k=6))}" for _ in range(num_cliques)]

    # Configura o tamanho da figura
    plt.figure(figsize=(40, 30))

    # Desenha cada clique com uma cor única
    for i, c in enumerate(cliques):
        nx.draw_networkx_nodes(grafo, pos, nodelist=c, node_color=cores[i])

    # Desenha as arestas do grafo
    nx.draw_networkx_edges(grafo, pos, alpha=1.0)

    # Adiciona os rótulos dos nós (nome dos vértices)
    labels = {n: str(n) for n in grafo.nodes}  # Usando os nomes dos vértices
    nx.draw_networkx_labels(grafo, pos, labels=labels)

    # Configura título
    plt.title("Visualização do Grafo com Cliques Maximais Coloridos")
    plt.show()
