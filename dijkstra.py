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

    def busca_largura(self, inicio, fim):
        arvore_busca = []
        visitados = []
        fila = deque([inicio])
        fila.append(inicio)
        visitados.append(inicio)
        while (fila):
            vertice = fila.popleft()
            for vizinho in self.grafo.get(vertice, []):
                if vizinho == fim:
                    arvore_busca.append((vertice, vizinho))
                    visitados.append(vizinho)
                    return arvore_busca
                elif not (vizinho in visitados):
                    arvore_busca.append((vertice, vizinho))
                    visitados.append(vizinho)
                    fila.append(vizinho)

    def dijkstra(self, inicio):
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

            for vizinho in self.grafo.get(atual,[]):
                destino = vizinho[0]
                peso = vizinho[1]

                if destino in visitados:
                    continue

                novo_custo = custo + peso

                min_arvore.inserir((destino,novo_custo,atual))
        return caminhos, visitados
            
    #verifico todos os possiveis caminho
    #veja qual é o menor caminho(leva min_heap)
    #marco o novo vertice
    #tiro todos os outros caminho que poderiam chagar nele
    #volto pro começo

grafo_feio = {
    'A': [['B', 1, 'A'], ['C', 2, 'A']],
    'B': [['A', 1, 'B']],
    'C': [['A', 2, 'C'], ['D', 3, 'C']],
    'D': [['C', 3, 'D']]
}

grafo_bonito ={
    's': [['2', 9, 's'],['6',14,'s'],['7',15,'s']],
    '2': [['3',23,'2']],
    '6': [['3', 18, '6'], ['5', 30, '6'], ['7',5,'6']],
    '7': [['5',20,'7'], ['t',44,'7']],
    '3': [['5',2,'3'], ['t',19,'3']],
    '5': [['4', 11,'5'], ['t',16,'5']],
    '4': [['3', 6,'4'], ['t',6,'4']] 
}

grafo = Grafo(grafo_bonito)

primeiro = 's'

p = grafo.dijkstra(primeiro)

print(p)
