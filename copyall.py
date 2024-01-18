import tkinter as tk
import ctypes
import sys
from tkinter import filedialog, messagebox
import subprocess

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if not is_admin():
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    sys.exit()

def escolher_pasta_origem():
    global caminhos
    root = tk.Tk()
    root.withdraw()  # Oculta a janela principal

    pasta_origem = filedialog.askdirectory(title='Selecionar Pasta de Origem')

    caminhos.append(pasta_origem)

def escolher_pasta_destino():
    global caminhos
    if len(caminhos) == 0:
        messagebox.showinfo('Pasta de origem não selecionada!', 'Selecione primeiro a pasta de origem dos arquivos!')
    else:
        root = tk.Tk()
        root.withdraw()  # Oculta a janela principal

        pasta_destino = filedialog.askdirectory(title='Selecionar Pasta de Destino')

        caminhos.append(pasta_destino)

caminhos = []

def copiar():
    global caminhos
    print(caminhos)

    if len(caminhos) == 2:
        caminho_origem = caminhos[0]
        caminho_destino = caminhos[1]

        comando = f'robocopy "{caminho_origem}" "{caminho_destino}" /e'

        try:
            resultado = subprocess.run(['powershell', '-Command', comando], capture_output=True, text=True, check=True)
            print("Saída padrão:", resultado.stdout)

            if resultado.stderr:  # Exibir mensagem apenas se houver erro
                messagebox.showinfo('Aviso na cópia', f'Aviso durante a cópia:\n{resultado.stderr}')
            
        except subprocess.CalledProcessError as e:
            messagebox.showinfo('Erro na cópia', f'Erro ao executar o comando:\n{e.stderr}')

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
