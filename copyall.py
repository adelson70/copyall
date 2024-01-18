# Importando bibliotecas
import tkinter as tk
from tkinter.font import Font
import subprocess


# Criando objeto root
janela = tk.Tk()
# Titulo da janela
janela.title('copyall')

# Label onde usuario ira escolher uma pasta de origem para copiar
tk.Label(janela, text='Escolha a pasta de origem dos arquivos', font= ..., ).pack(pady=10)



# Label onde usuario ira escolher uma pasta de destino para a copia
tk.Label(janela, text='Escolha a pasta de destino para os arquivos copiados', font= ..., ).pack(pady=10)


janela.mainloop()