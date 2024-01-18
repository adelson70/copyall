# Importando bibliotecas
import tkinter as tk
from tkinter.font import Font
import subprocess
from tkinter import filedialog
from tkinter import messagebox

# Função para escolher o caminho da pasta
# De destino e origem
def escolher_pasta_origem():
    global caminhos
    root = tk.Tk()
    root.withdraw()  # Oculta a janela principal

    pasta_origem = filedialog.askdirectory()

    caminhos.append(pasta_origem)

def escolher_pasta_destino():
    global caminhos
    if len(caminhos) == 0:
        messagebox.showinfo('Pasta de origem não selecionada!', 'Selecione primeiro a pasta de origem dos arquivos!')

    else:
        root = tk.Tk()
        root.withdraw()  # Oculta a janela principal

        pasta_destino = filedialog.askdirectory()

        caminhos.append(pasta_destino)

caminhos = []

# Função para fazer a copia dos arquivos
def copiar():
    global caminhos
    
    if len(caminhos) == 2:
        caminho_origem = caminhos[0]
        caminho_destino = caminhos[1]

        comando = f'robocopy "{caminho_origem}" "{caminho_destino}" /e'

        try:
            resultado = subprocess.run(['powershell', '-Command', comando], capture_output=True, text=True, check=True)
            print(resultado.stdout)
        
        except subprocess.CalledProcessError as e:
            print(f"Erro ao executar o comando:\n{e.stderr}")




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