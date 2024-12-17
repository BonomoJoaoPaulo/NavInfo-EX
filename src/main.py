from main_menu import run_main_menu
from utils.general_functions import scrap_all_data


if __name__ == "__main__":
    print("Iniciando o sistema...")
    paranagua, santarem, santos = scrap_all_data()
    run_main_menu(paranagua, santarem, santos)
