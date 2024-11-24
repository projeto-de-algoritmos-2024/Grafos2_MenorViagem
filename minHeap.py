class min_heap:
    def __init__(self):
        self.arvore = []
    
    def esta_vazia(self):
        #verifica se a arvore esta vazia
        return len(self.arvore) == 0
    
    def raiz(self):
        if self.esta_vazia():
            return None
        return self.arvore[0]

    def inserir(self, valor):
        #adiciona na arvore na ultima posição
        self.arvore.append(valor)
        #faz o reposicionamento dos elementos cada o valor inserido seja melhor que seu pai até ele ser menor 
        self.sobe_valor(len(self.arvore) -1)
     
    def sobe_valor(self, valor):
        #pega o pai
        pai_valor = (valor-1)//2
        
        while pai_valor >= 0 and self.arvore[pai_valor][1] > self.arvore[valor][1]:
            #troca o elemento pai e o filho
            self.arvore[pai_valor], self.arvore[valor] = self.arvore[valor], self.arvore[pai_valor]
            #muda o valor para a chave que o pai estava
            valor = pai_valor
            #ve se o pai é menor que o filho
            pai_valor = (valor-1)//2
    
    def deleta_menor(self):
        if self.esta_vazia():
            return None
        
        #pega a raiz que é o menor valor
        menor_valor = self.arvore[0]
        #coloca o ultimo elemento na riz
        self.arvore[0] = self.arvore[-1]
        #remove o ultimo elemento
        self.arvore.pop()
        #reorganiza a arvore
        self.desce_valor(0)

        return menor_valor
    
    def desce_valor(self, valor):
        filho_esquerda = 2 * valor + 1
        filho_direita = 2 * valor + 2
        menor = valor

        #compara a raiz com os filhos
        if filho_esquerda < len(self.arvore) and self.arvore[filho_esquerda][1] < self.arvore[menor][1]:
            menor = filho_esquerda

        if filho_direita < len(self.arvore) and self.arvore[filho_direita][1] < self.arvore[menor][1]:
            menor = filho_direita
        
        #troca o pai e o filho caso o paiseja maior
        if menor != valor:
            self.arvore[valor], self.arvore[menor] = self.arvore[menor], self.arvore[valor]
            self.desce_valor(menor)
