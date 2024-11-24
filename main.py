
from grafo_utils import ler_grafo, grau_dos_vertices, coeficiente_aglomeracao
from bron_kerbosch import encontrar_cliques_maximais
from visualizacao import visualizar_grafo

# Função principal
def main():
    arquivo = 'soc-dolphins.mtx'  # Nome do arquivo contendo os dados dos golfinhos
    grafo = ler_grafo(arquivo)

    # Calcula e imprime o grau dos vértices
    grau_dos_vertices(grafo)
    
    # Identifica e imprime todos os cliques maximais
    encontrar_cliques_maximais(grafo)
    
    # Calcula e imprime o coeficiente de aglomeração de cada vértice e o coeficiente médio
    coeficiente_aglomeracao(grafo)
    
    # Visualiza o grafo com os cliques maximais coloridos
    visualizar_grafo(grafo)

if __name__ == "__main__":
    main()
