# Projeto Golfinhos

Disciplina: Teoria e Aplicação de Grafos 

Aluno: Thelma Evangelista dos Santos 

Matrícula: 231003513 

Professor: Díbio Borges

Este é um projeto que analisa grafos representando conexões entre golfinhos, identifica cliques maximais, calcula o coeficiente de aglomeração e visualiza o grafo. O arquivo de dados utilizado é o `soc-dolphins.mtx`, que contém as informações sobre as conexões entre golfinhos.

## Descrição

O projeto utiliza a biblioteca `networkx` para manipulação de grafos, `matplotlib `para visualização gráfica e `ramdom` para gerar cores aleatórias para os cliques. Ele executa as seguintes tarefas:

1. Lê o arquivo de dados e cria o grafo.
2. Calcula o grau (número de conexões) de cada vértice.
3. Identifica cliques maximais no grafo usando o algoritmo de Bron-Kerbosch com pivoteamento.
4. Avalia o coeficiente de aglomeração de cada vértice e calcula o valor médio.
5. Visualiza o grafo com os cliques maximais destacados.


## Instalação

1. **Baixar o projeto**:  
   Para começar, baixe o projeto no seu computador.

2. **Instalar as dependências**:  
   Execute no terminal o seguinte comando para instalar as dependências necessárias:
   ```bash
   pip install networkx matplotlib
   ```

      Se encontar problemas com o pip, digite:
      ```bash
      python -m ensurepip --upgrade
      python -m pip install --upgrade pip
      ```  


## Como Usar

1. Certifique-se de que arquivo soc-dolphins.mtx está na pasta onde o código está localizado.
2. No terminal, navegue até a página onde está salvo o projeto:
   ```bash
   cd ~/caminho/para/a/pasta/ProjetoGolfinhos
3. Execute o código:
   ```bash
   python3 main.py
   ```

## Funcionalidades 
**Função ler_grafo:** Lê o arquivo de dados soc-dolphins.mtx e cria um grafo com os vértices e arestas.

**Função grau_dos_vertices:** Calcula o grau (número de conexões) de cada vértice.

**Função bron_kerbosch_pivoteamento:** Implementa o algoritmo de Bron-Kerbosch com pivoteamento para encontrar cliques maximais.

**Função coeficiente_aglomeracao:** Calcula o coeficiente de aglomeração de cada vértice.

**Função visualizar_grafo:** Exibe o grafo com os cliques maximais coloridos.

## Exemplo de Saída

Ao rodar o código, você verá as seguintes informações no terminal:

1. Graus dos vértices.

2. Cliques maximais encontrados no grafo.

3. Coeficiente de aglomeração de cada vértice e o coeficiente médio de aglomeração.

4. Visualização gráfica do grafo com os cliques coloridos.

## Dependências

**networkx:** Para manipulação e análise de grafos.

**matplotlib:** Para visualização gráfica do grafo.

**random:** Para gerar valores aleatórios. 

## Configuarações da máquina e Linguagem:
```bash
   python3
   mac OS 
   ``` 
