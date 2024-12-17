import tkinter as tk

from utils.santarem_functions import compare_quantities_by_goods, compare_quantities_by_goods_simplificado, compare_arrivals_over_time, compare_status_distribution, compare_quantities_by_status

def create_santarem_frame(container, show_frame, menu_frame):
    santarem_frame = tk.Frame(container)

    santarem_header = tk.Label(santarem_frame, text="SANTARÉM - OPÇÕES AVANÇADAS", font=("Arial", 14), pady=10)
    santarem_header.pack()

    santarem_option1 = tk.Button(santarem_frame, text="Quantidade por Mercadoria", font=("Arial", 12), command=compare_quantities_by_goods)
    santarem_option1.pack(pady=5)

    santarem_option5 = tk.Button(santarem_frame, text="Quantidade por Mercadoria Simplificadas", font=("Arial", 12), command=compare_quantities_by_goods_simplificado)
    santarem_option5.pack(pady=5)
    
    santarem_option2 = tk.Button(santarem_frame, text="Linha Temporal", font=("Arial", 12), command=compare_arrivals_over_time)
    santarem_option2.pack(pady=5)
    
    santarem_option3 = tk.Button(santarem_frame, text="Distribuição de Status", font=("Arial", 12), command=compare_status_distribution)
    santarem_option3.pack(pady=5)
    
    santarem_option4 = tk.Button(santarem_frame, text="Quantidades por Status", font=("Arial", 12), command=compare_quantities_by_status)
    santarem_option4.pack(pady=5)
    
    btn_back_to_menu = tk.Button(santarem_frame, text="Voltar ao menu principal", font=("Arial", 12), command=lambda: show_frame(menu_frame))
    btn_back_to_menu.pack(pady=20)

    return santarem_frame
