
# Baseado em: https://www.geeksforgeeks.org/maximal-clique-problem-recursive-solution/?ref=header_outind


def bron_kerbosch_pivoteamento(R, P, X, grafo):
    resultados = []
    
    # Se P e X estiverem vazios, encontramos um clique máximo
    if not P and not X:
        resultados.append(R)
        return resultados
    
    # Escolhe um vértice pivô de P ⋃ X
    u = next(iter(P.union(X)))  # Escolhe um vértice arbitrário de P ⋃ X
    
    # Para cada vértice v em P \ N(u), recursivamente busca cliques
    for v in P.difference(grafo[u]):
        novos_resultados = bron_kerbosch_pivoteamento(
            R.union({v}),
            P.intersection(grafo[v]),
            X.intersection(grafo[v]),
            grafo
        )
        resultados.extend(novos_resultados)  # Adiciona os novos cliques encontrados aos resultados
        P.remove(v)  # Remove v de P
        X.add(v)  # Adiciona v a X para evitar que seja processado novamente
    
    return resultados

def encontrar_cliques_maximais(grafo):
    R = set()  # Clique em construção
    P = set(grafo.nodes)  # Todos os vértices são P iniciais
    X = set()  # Nenhum vértice foi processado ainda
    cliques = bron_kerbosch_pivoteamento(R, P, X, grafo)
    print("Cliques maximais encontrados:", cliques)
    print("LEN CLIQUES", len(cliques))
