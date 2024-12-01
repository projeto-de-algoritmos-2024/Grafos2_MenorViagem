from collections import deque
import minHeap


class Grafo:

    # inicializa grafo
    def __init__(self, grafo=None):
        # inicializa novo grafo vazio se não encontrar grafo existente
        if grafo is None:
            grafo = {}
        # grafo = dicionário já criado
        self.grafo = grafo

    def dijkstra(self, inicio, fim):
        min_arvore = minHeap.min_heap()
        min_arvore.inserir((inicio,0, inicio))

        visitados = []
        caminhos = []
        
        while not min_arvore.esta_vazia():
            vertice = min_arvore.deleta_menor()
            atual = vertice[0]
            custo = vertice[1]

            if atual in visitados:
                continue
                
            visitados.append(atual)
            caminhos.append(vertice)

            # determina o fim da busca: se cheguei no meu destino, o algoritmo para de expandir a mancha
            if atual == fim:
                break

            for vizinho in self.grafo.get(atual,[]):
                destino = vizinho[0]
                peso = vizinho[1]

                if destino in visitados:
                    continue

                novo_custo = custo + peso

                min_arvore.inserir((destino,novo_custo,atual))

        caminhos.reverse()

        caminho_certo = []
        caminho_certo.append(caminhos[0])

        meu_tamanho = len(caminhos)

        minha_aresta = caminhos.pop(0)
        # enquanto a distância for diferente de 0 (que significa que podemos finalizar o backtracking)
        while minha_aresta[1] != 0:
            # percorrendo a lista inteira de possiveis caminhos
            for i in range (meu_tamanho-1):
                if caminhos[i][0] == minha_aresta[2]:
                    minha_aresta = caminhos[i]
                    caminho_certo.append(minha_aresta)


        #print(caminho_certo)
        # remove ['destino', 0, 'destino']
        caminho_certo.pop()
        return caminho_certo, visitados
