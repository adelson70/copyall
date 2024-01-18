import tkinter as tk
import ctypes
import sys
from tkinter import filedialog, messagebox
import subprocess

# Função para verificar se a aplicação esta sendo executada com privilegios adm
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

# Se não tiver privilegios sera reiniciado pedindo credenciais de adm
if not is_admin():
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    sys.exit()

# Função para ajustar a janela principal conforme o conteudo que estiver nela
def ajustar_janela_ao_conteudo(root):
    root.update_idletasks()  # Atualiza a geometria da janela
    largura = root.winfo_reqwidth()  # Largura requisitada pelo conteúdo
    altura = root.winfo_reqheight()  # Altura requisitada pelo conteúdo

    # Obtém as dimensões da tela
    largura_tela = root.winfo_screenwidth()
    altura_tela = root.winfo_screenheight()

    # Calcula a posição para centralizar a janela
    x_pos = (largura_tela - largura) // 2
    y_pos = (altura_tela - altura) // 2

    # Define a geometria da janela
    root.geometry(f"{largura+100}x{altura}+{x_pos}+{y_pos-130}")

# Função para escolher a pasta de origem dos arquivos a serem copiados
def escolher_pasta_origem():
    global caminhos
    root = tk.Tk()
    root.withdraw()  # Oculta a janela principal

    pasta_origem = filedialog.askdirectory(title='Selecionar Pasta de Origem')

    caminhos.append(pasta_origem)

# Função para escolher a pasta de destino dos arquivos que serão copiados
def escolher_pasta_destino():
    global caminhos

    # Caso o usuário não tenha escolhido a pasta de origem antes da pasta de destino
    if len(caminhos) == 0:
        messagebox.showinfo('Pasta de origem não selecionada!', 'Selecione primeiro a pasta de origem dos arquivos!')
    else:
        root = tk.Tk()
        root.withdraw()  # Oculta a janela principal

        pasta_destino = filedialog.askdirectory(title='Selecionar Pasta de Destino')

        caminhos.append(pasta_destino)

# Variavel lista que ira receber o caminho de origem e o caminho de destino
caminhos = []

# Função que ira executar a copia dos arquivos
def copiar():
    global caminhos
    print(caminhos)

    # Se o usúario fez a seleção de ambas as pastas
    if len(caminhos) == 2:
        caminho_origem = caminhos[0]
        caminho_destino = caminhos[1]
        comando = f'robocopy "{caminho_origem}" "{caminho_destino}" /e'

        subprocess.run(['powershell', '-Command', comando])
        caminhos.clear()

        messagebox.showinfo('Arquivos Copiados', 'Todos os arquivos foram copiados!')
    else:
        messagebox.showinfo('Pasta de destino incorreta', 'Escolha uma pasta de destino!')


# Criando objeto root
janela = tk.Tk()
janela.title('copyall')

tk.Label(janela, text='Escolha a pasta de origem dos arquivos').pack(pady=10)
tk.Button(janela, text='Escolher pasta de origem', command=lambda: escolher_pasta_origem()).pack(pady=10)

tk.Label(janela, text='Escolha a pasta de destino para os arquivos copiados').pack(pady=10)
tk.Button(janela, text='Escolher pasta de destino', command=lambda: escolher_pasta_destino()).pack(pady=10)

tk.Button(janela, text='copyall!', command=lambda: copiar()).pack(pady=10)

janela.mainloop()
