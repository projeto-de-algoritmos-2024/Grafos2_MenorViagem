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
            
    #verifico todos os possiveis caminho
    #veja qual é o menor caminho(leva min_heap)
    #marco o novo vertice
    #tiro todos os outros caminho que poderiam chagar nele
    #volto pro começo

# grafo_feio = {
#     'A': [['B', 1, 'A'], ['C', 2, 'A']],
#     'B': [['A', 1, 'B']],
#     'C': [['A', 2, 'C'], ['D', 3, 'C']],
#     'D': [['C', 3, 'D']]
# }

# grafo_bonito ={
#     's': [['2', 9, 's'],['6',14,'s'],['7',15,'s']],
#     '2': [['3',23,'2']],
#     '6': [['3', 18, '6'], ['5', 30, '6'], ['7',5,'6']],
#     '7': [['5',20,'7'], ['t',44,'7']],
#     '3': [['5',2,'3'], ['t',19,'3']],
#     '5': [['4', 11,'5'], ['t',16,'5']],
#     '4': [['3', 6,'4'], ['t',6,'4']] 
# }

# grafo = Grafo(grafo_bonito)

# primeiro = '5'
# fim = 't'

# p = grafo.dijkstra(primeiro, fim)

# print(p)
