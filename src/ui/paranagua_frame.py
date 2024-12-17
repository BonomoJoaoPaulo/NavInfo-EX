import tkinter as tk

from utils.paranagua_functions import plot_mercadoria_vs_quantidade, plot_sentido_operacoes, plot_top_operadores, plot_prancha_por_embarcacao, plot_loa_vs_saldo

def create_paranagua_frame(container, show_frame, menu_frame):
    paranagua_frame = tk.Frame(container)

    paranagua_header = tk.Label(paranagua_frame, text="PARANAGUÁ - OPÇÕES AVANÇADAS", font=("Arial", 14), pady=10)
    paranagua_header.pack()

    paranagua_option1 = tk.Button(paranagua_frame, text="Quantidade vs. Mercadoria", font=("Arial", 12), command=plot_mercadoria_vs_quantidade)
    paranagua_option1.pack(pady=5)

    paranagua_option2 = tk.Button(paranagua_frame, text="LOA vs. Saldo", font=("Arial", 12), command=plot_loa_vs_saldo)
    paranagua_option2.pack(pady=5)
    
    paranagua_option3 = tk.Button(paranagua_frame, text="Prancha por Embarcação", font=("Arial", 12), command=plot_prancha_por_embarcacao)
    paranagua_option3.pack(pady=5)
    
    paranagua_option4 = tk.Button(paranagua_frame, text="Top Operadores", font=("Arial", 12), command=plot_top_operadores)
    paranagua_option4.pack(pady=5)
    
    paranagua_option5 = tk.Button(paranagua_frame, text="Sentido das Operac.", font=("Arial", 12), command=plot_sentido_operacoes)
    paranagua_option5.pack(pady=5)

    # Botões de navegação
    btn_back_to_menu = tk.Button(paranagua_frame, text="Voltar ao menu principal", font=("Arial", 12), command=lambda: show_frame(menu_frame))
    btn_back_to_menu.pack(pady=20)

    return paranagua_frame
