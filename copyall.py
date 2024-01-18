# Importando bibliotecas
import tkinter as tk
from tkinter.font import Font
import subprocess
from tkinter import filedialog

# Função para escolher o caminho da pasta
# De destino e origem
def escolher_pasta_origem():
    root = tk.Tk()
    root.withdraw()  # Oculta a janela principal

    pasta_origem = filedialog.askdirectory()

    return pasta_origem

def escolher_pasta_destino():
    root = tk.Tk()
    root.withdraw()  # Oculta a janela principal

    pasta_destino = filedialog.askdirectory()

    return pasta_destino

# Função para fazer a copia dos arquivos
def copiar():
    ...



# Criando objeto root
janela = tk.Tk()
# Titulo da janela
janela.title('copyall')

# Label onde usuario ira escolher uma pasta de origem para copiar
tk.Label(janela, text='Escolha a pasta de origem dos arquivos', font= ..., ).pack(pady=10)

# Botão para escolher a pasta de origem dos arquivos
tk.Button(janela, text='Escolher pasta de origem', font=..., command=lambda: escolher_pasta_origem()).pack(pady=10)

# Label onde usuario ira escolher uma pasta de destino para a copia
tk.Label(janela, text='Escolha a pasta de destino para os arquivos copiados', font= ..., ).pack(pady=10)

# Botão para escolher a pasta de destino dos arquivos
tk.Button(janela, text='Escolher pasta de origem', font=..., command=lambda: escolher_pasta_destino()).pack(pady=10)


# Botão para iniciar ação de copia
tk.Button(janela, text='copyall!', font=..., command=lambda: escolher_pasta_destino()).pack(pady=10)


janela.mainloop()