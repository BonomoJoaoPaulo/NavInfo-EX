import tkinter as tk
from tkinter import messagebox

from ui.paranagua_frame import create_paranagua_frame
from ui.santarem_frame import create_santarem_frame
from ui.santos_frame import create_santos_frame
from utils.general_functions import export_all_data_as_csv, export_all_data_as_json

def ask_user_want_to_close():
    return messagebox.askyesno("Encerrar", "Deseja encerrar o sistema?")

# Função principal
def run_main_menu(paranagua, santarem, santos):
    # Função para trocar de tela
    def show_frame(frame):
        frame.tkraise()

    # Configuração da janela principal
    root = tk.Tk()
    root.title("Line-up de Navios")
    root.geometry("350x400")

    # Configuração do container de frames
    container = tk.Frame(root)
    container.pack(fill="both", expand=True)

    # Criando o frame do menu principal
    menu_frame = tk.Frame(container)
    menu_frame.grid(row=0, column=0, sticky="nsew")

    # Criando os frames das telas de cada porto
    paranagua_frame = create_paranagua_frame(container, show_frame, menu_frame)
    paranagua_frame.grid(row=0, column=0, sticky="nsew")
    
    santarem_frame = create_santarem_frame(container, show_frame, menu_frame)
    santarem_frame.grid(row=0, column=0, sticky="nsew")
    
    santos_frame = create_santos_frame(container, show_frame, menu_frame)
    santos_frame.grid(row=0, column=0, sticky="nsew")

    # Tela principal (menu_frame)
    header = tk.Label(menu_frame, text="LINEUP DE NAVIOS\nPortos de Paranaguá, Santarém e Santos", font=("Arial", 14), pady=10)
    header.pack()

    btn_csv = tk.Button(menu_frame, text="Exportar todos dados como CSV", font=("Arial", 12), command=lambda: export_all_data_as_csv(paranagua, santarem, santos))
    btn_csv.pack(pady=5)

    btn_json = tk.Button(menu_frame, text="Exportar todos dados como JSON", font=("Arial", 12), command=lambda: export_all_data_as_json(paranagua, santarem, santos))
    btn_json.pack(pady=5)
    
    btn_paranagua_screen = tk.Button(menu_frame, text="Paranaguá - Visualizar opções avançadas", font=("Arial", 12), command=lambda: show_frame(paranagua_frame))
    btn_paranagua_screen.pack(pady=5)
        
    btn_santarem_screen = tk.Button(menu_frame, text="Santarém - Visualizar opções avançadas", font=("Arial", 12), command=lambda: show_frame(santarem_frame))
    btn_santarem_screen.pack(pady=5)
    
    btn_santos_screen = tk.Button(menu_frame, text="Santos - Visualizar opções avançadas", font=("Arial", 12), command=lambda: show_frame(santos_frame))
    btn_santos_screen.pack(pady=5)

    btn_exit_menu = tk.Button(menu_frame, text="Sair", font=("Arial", 12), command=lambda: root.destroy() if ask_user_want_to_close() else None)
    btn_exit_menu.pack(pady=20)

    footer = tk.Label(menu_frame, text="Sistema de Gerenciamento de Navios", font=("Arial", 10), pady=10)
    footer.pack(side=tk.BOTTOM)

    # Mostra o menu principal inicialmente
    show_frame(menu_frame)

    # Executa a interface
    root.mainloop()
