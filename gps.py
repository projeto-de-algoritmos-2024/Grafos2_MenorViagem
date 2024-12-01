import tkinter as tk
import coordenadasMapa
import meuMapa
import math
import minhas_cidades
import dijkstra

c = dijkstra.Grafo(meuMapa.mapa)

meu_custo = 0

def cidades_no_caminho(caminho):
    jornada = []
    caminho_realizado = caminho[0]
    passando = caminho_realizado[0][0]
    jornada.append(passando)

    for cidade in caminho_realizado:
       if passando == cidade[0]:
           passando = cidade[2]
           jornada.append(passando)

    global meu_custo
    meu_custo = int(caminho_realizado[0][1]) * meu_custo
    print(meu_custo)
    custo_caminho.config(text = "O custo da viagem será de "+str(meu_custo))
    return jornada


def manipula_entrada(lista_cidades):
    
    lista_cidades_grafo = []
    # separa por virgula
    cidades_destino_origem = [p.strip() for p in lista_cidades.split(",")]
    print("Cidades digitadas:", cidades_destino_origem)

    # transforma a lista de compras em numeros que o grafo entende como seus nos, faz a legenda 
    for cidade in cidades_destino_origem:
        for minha_cidade in minhas_cidades.cidades:
            if minhas_cidades.cidades[minha_cidade] == cidade:
                lista_cidades_grafo.append(minha_cidade)
    
    global meu_custo 
    meu_custo = float(cidades_destino_origem[-1])
    print(lista_cidades_grafo)
    return lista_cidades_grafo

def desenha_caminho(jornada):
    raio_no = 10
    tamanho_seta = (15, 20, 6)
    # Conjunto de pares consecutivos da jornada para rápida verificação
    pares_jornada = set(zip(jornada, jornada[1:]))
    # Desenho dos vértices
    for node, edges in meuMapa.mapa.items():
        if(node in jornada):
            color = 'green'
        else:
            color='red'

        x, y = coordenadasMapa.coordenadas_mapa[node]
        canvas.create_oval(x-10, y-10, x+10, y+10, fill=color)
        canvas.create_text(x, y, text=node, fill="white")

    # Desenho das arestas com setas
    for node, edges in meuMapa.mapa.items():
        x1, y1 = coordenadasMapa.coordenadas_mapa[node]
        
        for neighbor, peso, _ in edges:
            x2, y2 = coordenadasMapa.coordenadas_mapa[neighbor]

            # Verificar se a aresta atual conecta pares consecutivos
            if (node, neighbor) in pares_jornada or (neighbor, node) in pares_jornada:
                color = 'green'
            else:
                color = 'gray'

            # Calcular direção e ajustar para evitar sobreposição
            dx, dy = x2 - x1, y2 - y1
            dist = math.sqrt(dx**2 + dy**2)
            dx, dy = dx / dist, dy / dist  # Vetor normalizado
            x1_adjusted, y1_adjusted = x1 + dx * raio_no, y1 + dy * raio_no
            x2_adjusted, y2_adjusted = x2 - dx * raio_no, y2 - dy * raio_no

            canvas.create_line(
                x1_adjusted, y1_adjusted, x2_adjusted, y2_adjusted,
                width=2, fill=color, arrow="last", arrowshape=tamanho_seta
            )

            # Exibindo o peso da aresta no meio
            meio_x = (x1_adjusted + x2_adjusted) / 2
            meio_y = (y1_adjusted + y2_adjusted) / 2
            canvas.create_text(meio_x, meio_y, text=str(peso), fill="black")

def gerenciador():
    a = entrada.get()
    b = manipula_entrada(a)
    caminho = dijkstra.Grafo.dijkstra(c, b[0], b[1])
    jornada = cidades_no_caminho(caminho)
    desenha_caminho(jornada,)

rota = tk.Tk()
rota.title("Mapa da Cidade")

produtos_aceitos = tk.Label(
    rota,
    text="Bem-vindo ao melhor gps da região de Eryndor"
)

produtos_aceitos.pack(pady=5)

titulo = tk.Label(rota, text="De onde vc esta saindo e pra onde vc deseja ir? 1 - Astrivana, 2 - Lunária, 3 - Eldrinor, 4 - Zirvanis, 5 - Norvalia, 6 - Erivale, 7 - Calthera, 8 - Drakmond, 9 - Silvaris, \n10 - Fenlaria, 11 - Torvindal, 12 - Krymora, 13 - Arvendil, 14 - Orynthia, 15 - Solthar, 16 - Quarion, 17 - Halveron, 18 - Morvanya, 19 - Velindre, \n20 - Galadore, 21 - Zyntheris, 22 - Etharion, 23 - Braxmoor, 24 - Lythoria, 25 - Eldenvale, 26 - Nyxhaven, 27 - Peryndor, 28 - Faeloria, 29 - Vorkalis, \n30 - Tharnwick, 31 - Myranor, 32 - Candralis, 33 - Arkeshal, 34 - Durnholde, 35 - Lymeris, 36 - Valtaren, 37 - Feronir, 38 - Talsyndra, 39 - Arwintha, \n40 - Drelmor, 41 - Cyrithal, 42 - Veskaris, 43 - Xeloria, 44 - Quindrel, 45 - Zaldara, 46 - Renfrost, 47 - Thalmyra, 48 - Ylverton, 49 - Fenwicke, 50 - Astrellyn.\n Digite a cidade de origem, a cidade de destino e custo do alimento do cavalo por quilômetro (usando o separador . e não vírgula para decimais), nessa ordem, separadas por vírgula e sem espaços.")
titulo.pack(pady=5)

entrada = tk.Entry(rota, width=50)
entrada.pack(pady=5)

botao = tk.Button(rota, text="Enviar", command=gerenciador)
botao.pack(pady=5)

custo_caminho = tk.Label(rota, text="")
custo_caminho.pack(pady=5)

canvas = tk.Canvas(rota, width=1050, height=500, bg="white")
canvas.pack()

rota.mainloop()
