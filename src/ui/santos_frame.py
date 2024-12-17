import tkinter as tk

from utils.santos_functions import plot_peso_total_por_mercadoria, plot_navios_por_bandeiras, plot_operacoes_por_agencia, plot_proporcao_navios_por_operacao, plot_linha_do_tempo

def create_santos_frame(container, show_frame, menu_frame):
    santos_frame = tk.Frame(container)

    santos_header = tk.Label(santos_frame, text="SANTOS - OPÇÕES AVANÇADAS", font=("Arial", 14), pady=10)
    santos_header.pack()

    santos_option1 = tk.Button(santos_frame, text="Peso Total por Mercadoria", font=("Arial", 12), command=plot_peso_total_por_mercadoria)
    santos_option1.pack(pady=5)

    santos_option2 = tk.Button(santos_frame, text="Total Navios por Bandeira", font=("Arial", 12), command=plot_navios_por_bandeiras)
    santos_option2.pack(pady=5)

    santos_option3 = tk.Button(santos_frame, text="Operações por Agência", font=("Arial", 12), command=plot_operacoes_por_agencia)
    santos_option3.pack(pady=5)
    
    santos_option4 = tk.Button(santos_frame, text="Proporção de Navios por Operação", font=("Arial", 12), command=plot_proporcao_navios_por_operacao)
    santos_option4.pack(pady=5)
    
    santos_option5 = tk.Button(santos_frame, text="Linha do Tempo", font=("Arial", 12), command=plot_linha_do_tempo)
    santos_option5.pack(pady=5)

    btn_back_to_menu = tk.Button(santos_frame, text="Voltar ao menu principal", font=("Arial", 12), command=lambda: show_frame(menu_frame))
    btn_back_to_menu.pack(pady=20)

    return santos_frame
