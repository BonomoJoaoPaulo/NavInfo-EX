import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from utils.general_functions import get_most_recent_file

def plot_peso_total_por_mercadoria():
    directory = "../data/csv"
    file_prefix = "santos_ships"
    recent_file = get_most_recent_file(directory, file_prefix)
    df = pd.read_csv(recent_file, delimiter=",")
    
    df["PesoWeight"] = pd.to_numeric(df["PesoWeight"], errors="coerce")
    peso_por_mercadoria = df.groupby("MercadoriaGoods")["PesoWeight"].sum().sort_values(ascending=False)

    plt.figure(figsize=(10, 6))
    peso_por_mercadoria.plot(kind="bar", color="lightgreen")
    plt.title("Peso Total Transportado por Mercadoria")
    plt.xlabel("Mercadoria")
    plt.ylabel("Peso Total")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_navios_por_bandeiras():
    directory = "../data/csv"
    file_prefix = "santos_ships"
    recent_file = get_most_recent_file(directory, file_prefix)
    df = pd.read_csv(recent_file, delimiter=",")

    bandeiras_count = df["BandeiraFlag"].value_counts()

    plt.figure(figsize=(10, 6))
    bandeiras_count.plot(kind="bar", color="skyblue")
    plt.title("Quantidade de Navios por Bandeira")
    plt.xlabel("Bandeira")
    plt.ylabel("Quantidade de Navios")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_operacoes_por_agencia():
    directory = "../data/csv"
    file_prefix = "santos_ships"
    recent_file = get_most_recent_file(directory, file_prefix)
    df = pd.read_csv(recent_file, delimiter=",")

    operacoes_por_agencia = df["AgênciaOffice"].value_counts()

    plt.figure(figsize=(12, 6))
    operacoes_por_agencia.plot(kind="bar", color="coral")
    plt.title("Número de Operações por Agência")
    plt.xlabel("Agência")
    plt.ylabel("Quantidade de Operações")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_proporcao_navios_por_operacao():
    directory = "../data/csv"
    file_prefix = "santos_ships"
    recent_file = get_most_recent_file(directory, file_prefix)
    df = pd.read_csv(recent_file, delimiter=",")

    navios_por_operacao = df["OperaçOperat"].value_counts()

    plt.figure(figsize=(8, 8))
    navios_por_operacao.plot(kind="pie", autopct="%1.1f%%", startangle=90, colors=sns.color_palette("Set2"))
    plt.title("Proporção de Navios por Tipo de Operação")
    plt.ylabel("")
    plt.tight_layout()
    plt.show()

def plot_linha_do_tempo():
    directory = "../data/csv"
    file_prefix = "santos_ships"
    recent_file = get_most_recent_file(directory, file_prefix)
    df = pd.read_csv(recent_file, delimiter=",")
    
    df["Cheg/Arrivald/m/y"] = pd.to_datetime(df["Cheg/Arrivald/m/y"], errors="coerce")

    chegadas_por_dia = df["Cheg/Arrivald/m/y"].dt.date.value_counts().sort_index()

    plt.figure(figsize=(10, 6))
    chegadas_por_dia.plot(kind="line", marker="o", color="blue")
    plt.title("Chegadas de Navios por Mês")
    plt.xlabel("Data")
    plt.ylabel("Quantidade de Navios")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
