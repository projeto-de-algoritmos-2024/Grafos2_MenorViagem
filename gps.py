import tkinter as tk
import coordenadasMapa
import meuMapa

def desenha_caminho():
    # Desenho dos vértices
    for node, edges in meuMapa.mapa.items():
        x, y = coordenadasMapa.coordenadas_mapa[node]
        canvas.create_oval(x-10, y-10, x+10, y+10, fill='blue')
        canvas.create_text(x, y, text=node, fill="white")

    # Desenho das arestas com setas
    for node, edges in meuMapa.mapa.items():
        x1, y1 = coordenadasMapa.coordenadas_mapa[node]
        for neighbor, peso, _ in edges:
            x2, y2 = coordenadasMapa.coordenadas_mapa[neighbor]
            canvas.create_line(x1, y1, x2, y2, width=2, fill="gray", arrow="last")
            # Exibindo o peso da aresta no meio
            meio_x = (x1 + x2) / 2
            meio_y = (y1 + y2) / 2
            canvas.create_text(meio_x, meio_y, text=str(peso), fill="black")

def gerenciador():
    desenha_caminho()

rota = tk.Tk()
rota.title("Mapa da Cidade")

produtos_aceitos = tk.Label(
    rota,
    text="Bem-vindo ao melhor gps da cidade"
)

produtos_aceitos.pack(pady=10)

titulo = tk.Label(rota, text="De onde vc esta saindo e pra onde vc deseja ir?")
titulo.pack(pady=10)

entrada = tk.Entry(rota, width=50)
entrada.pack(pady=5)

botao = tk.Button(rota, text="Enviar", command=gerenciador)
botao.pack(pady=10)

coordenadas_caminho = tk.Label(rota, text="")
coordenadas_caminho.pack(pady=10)

canvas = tk.Canvas(rota, width=1050, height=500, bg="white")
canvas.pack()

rota.mainloop()
