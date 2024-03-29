import tkinter as tk
import ctypes
import sys
from tkinter import filedialog, messagebox
import subprocess
import psutil

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
    root.geometry(f"{largura+100}x{altura+10}+{x_pos}+{y_pos-130}")

# Variaveis lista que irão receber o caminho de origem e o caminho de destino
caminho_origem = []
caminho_destino = []

# Função para escolher a pasta de origem dos arquivos a serem copiados
def escolher_pasta_origem():
    global caminho_origem
    caminho_origem.clear()

    pasta_origem = filedialog.askdirectory(title='Selecionar Pasta de Origem')

    # Tratamento de erro caso o usuario não selecione nenhuma pasta
    if len(pasta_origem) > 1:
        caminho_origem.append(pasta_origem)

# Função para escolher a pasta de destino dos arquivos que serão copiados
def escolher_pasta_destino():
    global caminho_destino
    caminho_destino.clear()
    
    pasta_destino = filedialog.askdirectory(title='Selecionar Pasta de Destino')

    # Tratamento de erro caso o usuario não selecione nenhuma pasta
    if len(pasta_destino) > 1:
        caminho_destino.append(pasta_destino)

# Função que ira executar a copia dos arquivos
def copiar():
    global caminho_origem
    global caminho_destino

    # Se o usúario fez a seleção de ambas as pastas
    if len(caminho_origem) and len(caminho_destino) == 1:
        print(len(caminho_destino))
        print(caminho_destino)

        comando = f'robocopy "{caminho_origem[-1]}" "{caminho_destino[-1]}" /e'

        processo = subprocess.run(['powershell', '-Command', comando])
        messagebox.showinfo('Arquivos Copiados', 'Todos os arquivos foram copiados!')

        # Tentamos encontrar e encerrar o processo PowerShell usando o psutil
        # Para que o progrma não fique executado em segundo plano depois de encerrar pela janela
        for proc in psutil.process_iter(['pid', 'name']):
            if 'powershell' in proc.info['name'].lower():
                try:
                    p = psutil.Process(proc.info['pid'])
                    p.terminate()
                except psutil.NoSuchProcess as e:
                    print(f'Erro ao encerrar o processo: {e}')


    else:
        messagebox.showerror('Erro', 'Escolha uma pasta de origem e destino!')


# Criando objeto root
janela = tk.Tk()
janela.title('CopyAll')


tk.Label(janela, text='Escolha a pasta de origem dos arquivos').pack(pady=5)
tk.Button(janela, text='Escolher pasta de origem', command=lambda: escolher_pasta_origem()).pack(pady=5)

# Espaço entre as labels
tk.Label(janela, text='').pack(pady=2)

tk.Label(janela, text='Escolha a pasta de destino para os arquivos copiados').pack(pady=10)
tk.Button(janela, text='Escolher pasta de destino', command=lambda: escolher_pasta_destino()).pack(pady=5)

# Espaço entre as labels
tk.Label(janela, text='').pack(pady=2)

tk.Button(janela, text='COPYALL!', command=lambda: copiar()).pack(pady=5)

ajustar_janela_ao_conteudo(janela)

# Para garantir que o programa sera encerrado
janela.protocol("WM_DELETE_WINDOW", janela.destroy)
janela.mainloop()