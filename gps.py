import tkinter as tk
import coordenadasMapa
import meuMapa
import math

def desenha_caminho():
    raio_no = 10
    tamanho_seta = (15, 20, 6)
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
            
            # Calcular direção e ajustar para evitar sobreposição
            dx, dy = x2 - x1, y2 - y1
            dist = math.sqrt(dx**2 + dy**2)
            dx, dy = dx / dist, dy / dist  # Vetor normalizado
            x1_adjusted, y1_adjusted = x1 + dx * raio_no, y1 + dy * raio_no
            x2_adjusted, y2_adjusted = x2 - dx * raio_no, y2 - dy * raio_no

            canvas.create_line(
                x1_adjusted, y1_adjusted, x2_adjusted, y2_adjusted,
                width=2, fill="gray", arrow="last", arrowshape=tamanho_seta
            )

            # Exibindo o peso da aresta no meio
            meio_x = (x1_adjusted + x2_adjusted) / 2
            meio_y = (y1_adjusted + y2_adjusted) / 2
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
