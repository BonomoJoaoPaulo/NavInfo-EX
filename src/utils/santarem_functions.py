import pandas as pd
import matplotlib
matplotlib.use('TkAgg')  # Força o uso do backend TkAgg para exibição interativa no tkinter
import matplotlib.pyplot as plt
from datetime import datetime

from utils.general_functions import get_most_recent_file
  
def compare_quantities_by_goods():
    directory = "../data/csv"
    file_prefix = "santarem_ships"
    recent_file = get_most_recent_file(directory, file_prefix)
    df = pd.read_csv(recent_file, delimiter=",")

    df["QUANTIDADE (T)"] = df["QUANTIDADE (T)"].str.replace(".", "").str.replace(",", ".")
    df["QUANTIDADE (T)"] = pd.to_numeric(df["QUANTIDADE (T)"], errors="coerce")

    mercadoria_totais = df.groupby("MERCADORIA")["QUANTIDADE (T)"].sum().sort_values()

    # Plotar
    plt.figure(figsize=(10, 6))
    mercadoria_totais.plot(kind="barh", color="skyblue")
    plt.title("Quantidades Totais por Tipo de Mercadoria")
    plt.xlabel("Quantidade (T)")
    plt.ylabel("Mercadoria")
    plt.tight_layout()
    plt.show()

def compare_quantities_by_goods_simplificado():
    directory = "../data/csv"
    file_prefix = "santarem_ships"
    recent_file = get_most_recent_file(directory, file_prefix)
    df = pd.read_csv(recent_file, delimiter=",")

    df["QUANTIDADE (T)"] = df["QUANTIDADE (T)"].str.replace(".", "").str.replace(",", ".")
    df["QUANTIDADE (T)"] = pd.to_numeric(df["QUANTIDADE (T)"], errors="coerce")

    df["MERCADORIA_SIMPLIFICADA"] = df["MERCADORIA"].str.split().str[0]
    mercadoria_totais = df.groupby("MERCADORIA_SIMPLIFICADA")["QUANTIDADE (T)"].sum().sort_values()

    # Plotar
    plt.figure(figsize=(10, 6))
    mercadoria_totais.plot(kind="barh", color="skyblue")
    plt.title("Quantidades Totais por Tipo de Mercadoria")
    plt.xlabel("Quantidade (T)")
    plt.ylabel("Mercadoria")
    plt.tight_layout()
    plt.show()

def compare_arrivals_over_time():
    directory = "../data/csv"
    file_prefix = "santarem_ships"
    recent_file = get_most_recent_file(directory, file_prefix)
    df = pd.read_csv(recent_file, delimiter=",")

    df["CHEGADA"] = pd.to_datetime(df["CHEGADA"], errors="coerce")
    chegadas_por_dia = df.groupby(df["CHEGADA"].dt.date).size()

    plt.figure(figsize=(12, 6))
    plt.plot(chegadas_por_dia.index, chegadas_por_dia.values, marker="o", color="green")
    plt.title("Fluxo de Chegadas ao Longo do Tempo")
    plt.xlabel("Data")
    plt.ylabel("Número de Chegadas")
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def compare_status_distribution():
    directory = "../data/csv"
    file_prefix = "santarem_ships"
    recent_file = get_most_recent_file(directory, file_prefix)
    df = pd.read_csv(recent_file, delimiter=",")
    
    status_counts = df["STATUS"].value_counts()

    plt.figure(figsize=(8, 8))
    plt.pie(status_counts, labels=status_counts.index, autopct="%1.1f%%", startangle=90, colors=plt.cm.Paired.colors)
    plt.title("Distribuição de Status das Embarcações")
    plt.show()

def compare_quantities_by_status():
    directory = "../data/csv"
    file_prefix = "santarem_ships"
    recent_file = get_most_recent_file(directory, file_prefix)
    df = pd.read_csv(recent_file, delimiter=",")

    df["QUANTIDADE (T)"] = df["QUANTIDADE (T)"].str.replace(".", "").str.replace(",", ".")
    df["QUANTIDADE (T)"] = pd.to_numeric(df["QUANTIDADE (T)"], errors="coerce")
    status_quantidades = df.groupby("STATUS")["QUANTIDADE (T)"].sum().sort_values()

    plt.figure(figsize=(10, 6))
    status_quantidades.plot(kind="bar", color="orange")
    plt.title("Quantidades Totais por Status de Embarcação")
    plt.xlabel("Status")
    plt.ylabel("Quantidade (T)")
    plt.tight_layout()
    plt.show()
